# AI-Powered Demand Forecasting System for Hyperlocal Delivery

## Overview
This project is an AI-powered demand forecasting system designed for hyperlocal delivery services (like Blinkit, Dunzo, Swiggy Instamart). It leverages historical sales data to predict future product demand, helping businesses optimize inventory, reduce waste, and prevent stockouts.

The application features a **Trend Analysis Dashboard**, **Forecasting Models** using Facebook Prophet, and a unique **Voice-Controlled Interface** for accessibility.

## Key Features
-   **📈 Demand Forecasting**: Predicts monthly sales for specific products using the Prophet time-series model.
-   **🗣️ Voice Control**: Ask for predictions using voice commands (e.g., "Tomato January").
-   **📊 Interactive Visualizations**:
    -   Compare past sales vs. forecasted demand.
    -   Analyze sales vs. stock levels.
    -   View seasonal trends (Diwali, Summer, etc.).
-   **📦 Hyperlocal Focus**: Tailored for high-frequency, location-specific retail data.

## 🛠️ Tech Stack
-   **💻 Language:** Python 🐍
-   **📚 Libraries:** Pandas 🐼, Prophet 
-   **📊 Visualization:** Plotly 📉, Streamlit 👑
-   **🗣️ Voice Integration:** SpeechRecognition 🎙️, pyttsx3 🔊

## Installation & Setup

### Prerequisites
-   Python 3.8 or higher
-   pip (Python package manager)

### Steps
1.  **Clone the Repository**
    ```bash
    git clone mhttps://github.com/Vivin888/Forecasting_System.git
    cd Forecasting_System-main
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    streamlit run Forecasting.py
    ```

4.  **Access the App**
    Open your browser and navigate to `http://localhost:8501`.

## Usage Guide
1.  **Main Dashboard**: Overview of the project and navigation.
2.  **Future Prediction**:
    -   Select a product and a month from the sidebar.
    -   View the predicted sales count and confidence intervals.
    -   Use the "Click to speak" button to request a forecast via voice.
3.  **Past Data**: Compare historical sales across different products for a specific month.
4.  **Past Data Visualization**: Detailed analytics on Sales vs. Stock, including cumulative trends and distribution.

## Dataset
The system uses `hyperlocal_demand_forecasting_with_grocery_items.xlsx`, containing:
-   **Monthly/Yearly Sales & Stock**: Data for various grocery items.
-   **Seasonal Markers**: Indicators for festivals and seasons affecting demand.


