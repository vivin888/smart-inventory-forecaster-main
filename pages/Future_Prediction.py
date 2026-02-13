import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go

# Try to import voice libraries (optional)
try:
    import speech_recognition as sr
    VOICE_INPUT_AVAILABLE = True
except ImportError:
    VOICE_INPUT_AVAILABLE = False
    
try:
    import pyttsx3
    VOICE_OUTPUT_AVAILABLE = True
except ImportError:
    VOICE_OUTPUT_AVAILABLE = False

# Load your data (ensure the file path is correct)
data = pd.read_excel('pages/hyperlocal_demand_forecasting_with_grocery_items.xlsx')

# Convert 'Month' to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Create a list of months sorted correctly
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

st.title("🔮 Future Demand Prediction")
st.markdown("Use AI-powered forecasting to predict future product demand")

# Voice input section (only if available)
if VOICE_INPUT_AVAILABLE:
    st.subheader("🎙️ Voice Input (Optional)")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎤 Speak Product & Month"):
            try:
                recognizer = sr.Recognizer()
                with sr.Microphone() as source:
                    st.info("Listening... Please say product name and month (e.g., 'Tomato January')")
                    audio = recognizer.listen(source, timeout=5)
                    text = recognizer.recognize_google(audio)
                    st.success(f"You said: {text}")
                    
                    # Try to parse the input
                    words = text.lower().split()
                    detected_product = None
                    detected_month = None
                    
                    for word in words:
                        # Check for product
                        for product in data['Product Name'].unique():
                            if word in product.lower():
                                detected_product = product
                                break
                        # Check for month
                        for month in months_list:
                            if word in month.lower():
                                detected_month = month
                                break
                    
                    if detected_product and detected_month:
                        st.session_state['voice_product'] = detected_product
                        st.session_state['voice_month'] = detected_month
                        
            except Exception as e:
                st.error(f"Error with voice input: {str(e)}")
else:
    st.info("💡 Voice input is not available. Install PyAudio and SpeechRecognition for voice features.")

# Manual selection
st.subheader("📊 Manual Selection")

# Use voice input if available, otherwise use default
default_product = st.session_state.get('voice_product', data['Product Name'].unique()[0])
default_month_idx = months_list.index(st.session_state.get('voice_month', 'January')) if st.session_state.get('voice_month') in months_list else 0

selected_product = st.selectbox("Select Product", data['Product Name'].unique(), 
                                index=list(data['Product Name'].unique()).index(default_product) if default_product in data['Product Name'].unique() else 0)
selected_month = st.selectbox("Select Month for Prediction", months_list, index=default_month_idx)

# Filter data for the selected product
product_data = data[data['Product Name'] == selected_product].copy()

if not product_data.empty:
    # Prepare data for Prophet
    df = product_data[['Month', 'Monthly_Sales']].rename(columns={'Month': 'ds', 'Monthly_Sales': 'y'})
    
    # Fit the Prophet model
    model = Prophet()
    model.fit(df)
    
    # Create future dataframe for prediction
    future = model.make_future_dataframe(periods=12, freq='M')
    forecast = model.predict(future)
    
    # Get the prediction for the selected month
    month_num = months_list.index(selected_month) + 1
    current_year = pd.Timestamp.now().year
    target_date = pd.Timestamp(year=current_year, month=month_num, day=1)
    
    # Find the closest prediction
    forecast['date_diff'] = abs(forecast['ds'] - target_date)
    closest_prediction = forecast.loc[forecast['date_diff'].idxmin()]
    
    predicted_value = closest_prediction['yhat']
    lower_bound = closest_prediction['yhat_lower']
    upper_bound = closest_prediction['yhat_upper']
    
    # Display prediction results
    st.subheader(f"📈 Prediction Results for {selected_product} in {selected_month}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Predicted Sales", f"{int(predicted_value):,}")
    with col2:
        st.metric("Lower Bound", f"{int(lower_bound):,}")
    with col3:
        st.metric("Upper Bound", f"{int(upper_bound):,}")
    
    # Confidence interval
    confidence = ((upper_bound - lower_bound) / predicted_value) * 100
    st.info(f"Confidence Interval: ±{confidence:.1f}%")
    
    # Voice output (only if available)
    if VOICE_OUTPUT_AVAILABLE:
        if st.button("🔊 Speak Prediction"):
            try:
                engine = pyttsx3.init()
                text = f"The predicted sales for {selected_product} in {selected_month} is {int(predicted_value)} units"
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                st.error(f"Error with voice output: {str(e)}")
    
    # Plot historical data and forecast
    st.subheader("📊 Historical Data and Forecast")
    
    fig = go.Figure()
    
    # Historical data
    fig.add_trace(go.Scatter(
        x=df['ds'], 
        y=df['y'],
        mode='lines+markers',
        name='Historical Sales',
        line=dict(color='blue', width=2)
    ))
    
    # Forecast
    fig.add_trace(go.Scatter(
        x=forecast['ds'], 
        y=forecast['yhat'],
        mode='lines',
        name='Forecast',
        line=dict(color='red', width=2, dash='dash')
    ))
    
    # Confidence interval
    fig.add_trace(go.Scatter(
        x=forecast['ds'].tolist() + forecast['ds'].tolist()[::-1],
        y=forecast['yhat_upper'].tolist() + forecast['yhat_lower'].tolist()[::-1],
        fill='toself',
        fillcolor='rgba(255,0,0,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='Confidence Interval'
    ))
    
    fig.update_layout(
        title=f'Sales Forecast for {selected_product}',
        xaxis_title='Date',
        yaxis_title='Sales',
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Additional insights
    st.subheader("💡 Insights")
    
    # Calculate trend
    recent_avg = df['y'].tail(3).mean()
    if predicted_value > recent_avg:
        trend = "📈 Increasing"
        trend_pct = ((predicted_value - recent_avg) / recent_avg) * 100
    else:
        trend = "📉 Decreasing"
        trend_pct = ((recent_avg - predicted_value) / recent_avg) * 100
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Trend", trend, f"{trend_pct:.1f}%")
    with col2:
        st.metric("Recent Average", f"{int(recent_avg):,}")
    
    # Recommendations
    st.subheader("💼 Recommendations")
    if predicted_value > recent_avg * 1.2:
        st.success("🔼 High demand expected! Consider increasing inventory.")
    elif predicted_value < recent_avg * 0.8:
        st.warning("🔽 Lower demand expected. Adjust inventory accordingly.")
    else:
        st.info("➡️ Stable demand expected. Maintain current inventory levels.")

else:
    st.error(f"No data available for {selected_product}")
