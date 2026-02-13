<div align="center">

# 🚀 AI-Powered Smart Inventory Forecaster

### *Predict Demand. Optimize Inventory. Maximize Profits.*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Prophet](https://img.shields.io/badge/Prophet-Forecasting-00D9FF?style=for-the-badge)](https://facebook.github.io/prophet/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**An intelligent demand forecasting system for hyperlocal delivery services**  
*Powered by Facebook Prophet | Voice-Enabled | Real-time Analytics*

[🎯 Features](#-key-features) • [🚀 Quick Start](#-installation--setup) • [📊 Demo](#-usage-guide) • [🛠️ Tech Stack](#️-tech-stack)

---

</div>

## 🌟 Overview

Transform your inventory management with **AI-powered demand forecasting**! This system is designed for hyperlocal delivery services (Blinkit, Dunzo, Swiggy Instamart, etc.) to predict future product demand using historical sales data.

### 💡 Why This Matters?
- ✅ **Reduce Waste** - Prevent overstocking and spoilage
- ✅ **Prevent Stockouts** - Never miss a sale opportunity
- ✅ **Optimize Inventory** - Data-driven purchasing decisions
- ✅ **Increase Profits** - Better resource allocation

---

## ✨ Key Features

### 🎯 **Core Functionality**
| Feature | Description |
|---------|-------------|
| 📈 **AI Forecasting** | Prophet-based time-series predictions with confidence intervals |
| 🗣️ **Voice Control** | Hands-free predictions via voice commands (e.g., "Tomato January") |
| 📊 **Interactive Dashboards** | Real-time visualizations with Plotly & Streamlit |
| 📦 **Hyperlocal Focus** | Optimized for high-frequency, location-specific retail |
| 🎨 **Multi-Page App** | Organized navigation with dedicated analysis pages |

### 📊 **Advanced Analytics**
- 📉 **Trend Analysis** - Historical sales patterns and seasonality
- 🔄 **Comparative Views** - Sales vs. Stock level analysis
- 📅 **Seasonal Insights** - Festival and event impact detection
- 📈 **Cumulative Trends** - Long-term demand patterns
- 🎯 **Confidence Intervals** - Prediction reliability metrics
- 💡 **Smart Recommendations** - Automated inventory suggestions

### 🎙️ **Accessibility Features**
- 🗣️ **Speech Recognition** - Voice input for predictions (optional)
- 🔊 **Text-to-Speech** - Audio feedback for results (optional)
- 🖱️ **One-Click Predictions** - Simple, intuitive interface
- 📱 **Responsive Design** - Works on desktop and mobile

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **ML/Analytics** | ![Prophet](https://img.shields.io/badge/Prophet-00D9FF?style=flat) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) |
| **Visualization** | ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) |
| **Voice AI** | ![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-4285F4?style=flat) ![pyttsx3](https://img.shields.io/badge/pyttsx3-TTS-orange?style=flat) ![PyAudio](https://img.shields.io/badge/PyAudio-green?style=flat) |
| **Data Processing** | ![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white) ![OpenPyXL](https://img.shields.io/badge/OpenPyXL-green?style=flat) |

</div>

---

## 🚀 Installation & Setup

### 📋 Prerequisites
- **Python** 3.8 or higher
- **pip** (Python package manager)
- **Microphone** (optional, for voice features)

### ⚡ Quick Start

```bash
# 1️⃣ Clone the Repository
git clone https://github.com/vivin888/smart-inventory-forecaster-main.git
cd smart-inventory-forecaster-main

# 2️⃣ Install Dependencies
pip install -r requirements.txt

# 3️⃣ (Optional) Install Voice Features
pip install pyaudio

# 4️⃣ Run the Application
streamlit run Forecasting.py

# 5️⃣ Open in Browser
# Navigate to http://localhost:8501
```

### � Dependencies

```txt
streamlit
pandas
prophet
plotly
SpeechRecognition
pyttsx3
openpyxl
pyaudio (optional - for voice features)
```

---

## 📊 Usage Guide

### 🏠 **Main Dashboard**
- Project overview and feature highlights
- Navigation to different analysis pages
- Quick access to forecasting tools

### 🔮 **Future Prediction** ⭐ NEW!
1. **Manual Selection:**
   - Select a **product** from the dropdown
   - Choose a **month** for prediction
   - View AI-generated forecast with confidence intervals

2. **Voice Mode** (if PyAudio installed):
   - Click "🎤 Speak Product & Month"
   - Say clearly: **"Tomato January"** or **"Canned Beans March"**
   - System automatically selects and predicts

3. **Results:**
   - Predicted sales with upper/lower bounds
   - Interactive historical + forecast chart
   - Trend analysis (Increasing/Decreasing)
   - Smart inventory recommendations
   - Voice output option

### 📈 **Past Data Analysis**
- Compare historical sales across products
- Filter by specific months
- Identify top-performing items
- Sales trends over time

### 📊 **Past Data Visualization**
- **Sales vs. Stock** comparison charts
- Cumulative trend analysis
- Distribution and pattern recognition
- Multiple chart types (Bar, Line, Area, Pie)

---

## 📁 Project Structure

```
smart-inventory-forecaster-main/
├── Forecasting.py                 # Main application entry point
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
│
├── pages/                         # Streamlit pages
│   ├── Future_Prediction.py      # AI forecasting with voice
│   ├── Past_Data.py              # Historical data analysis
│   ├── Past_Data_visualization.py # Advanced visualizations
│   └── hyperlocal_demand_forecasting_with_grocery_items.xlsx
│
└── jupyter file/                  # Development notebooks
    ├── month_forecasting.ipynb   # Forecasting experiments
    └── hyperlocal_demand_forecasting_with_grocery_items.xlsx
```

---

## 📁 Dataset

**File**: `hyperlocal_demand_forecasting_with_grocery_items.xlsx`

| Column | Description |
|--------|-------------|
| 📅 **Month** | Monthly timestamps |
| 🛒 **Product Name** | Grocery item names |
| 💰 **Monthly_Sales** | Historical sales counts |
| 📦 **Monthly_Stock** | Inventory levels |

**Sample Products:**
- Tomato, Canned Beans, Milk, Rice, Cooking Oil, and more

---

## 🎯 Use Cases

- 🏪 **Retail Stores** - Optimize inventory for grocery chains
- 🚚 **Delivery Services** - Predict demand for hyperlocal platforms
- 🏭 **Supply Chain** - Improve procurement planning
- 📊 **Business Analytics** - Data-driven decision making
- 🌾 **Agriculture** - Forecast crop demand and pricing

---

## 🎤 Voice Features Guide

### Setup
```bash
pip install pyaudio
```

### Usage
1. **Voice Input:**
   - Click "🎤 Speak Product & Month"
   - Speak clearly: "Product Month" (e.g., "Tomato January")
   - System recognizes and processes

2. **Voice Output:**
   - Click "🔊 Speak Prediction"
   - Hear prediction results aloud

### Troubleshooting
- Ensure microphone is connected and working
- Grant browser/system microphone permissions
- Check Windows sound settings
- Voice features work without PyAudio (shows info message)

---

## 🚀 Features Roadmap

- [x] AI-powered forecasting with Prophet
- [x] Voice input/output
- [x] Interactive visualizations
- [x] Multi-page navigation
- [x] Confidence intervals
- [x] Trend analysis
- [ ] Docker containerization
- [ ] API endpoints
- [ ] Multi-language support
- [ ] Mobile app
- [ ] Real-time data integration

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Vivin Rakul**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Vivin888)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- **Facebook Prophet** - Time series forecasting
- **Streamlit** - Web application framework
- **Plotly** - Interactive visualizations
- **Python Community** - Amazing libraries and support

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Made with ❤️ and Python**

</div>
