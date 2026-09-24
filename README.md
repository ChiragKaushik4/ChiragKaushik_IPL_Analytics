# 🏏 IPL Match Intelligence & Prediction Engine

## 📌 Project Overview
This project is an enterprise-grade, real-time Machine Learning dashboard that predicts the win probability of chasing teams in the Indian Premier League (IPL). Built with a clean, broadcast-style UI, it transforms live match telemetry into actionable sports analytics.

## 🚀 Key Features
* **Real-Time Win Probability:** Powered by a trained Random Forest Classifier (`pipe.pkl`).
* **Tactical Pressure Index:** An explainable AI (XAI) radar chart visualizing the pressure of the Required Run Rate, Wickets Lost, and Target Load.
* **Momentum Simulator:** A "What-If" sensitivity analysis engine that calculates how the exact next delivery (e.g., hitting a Six vs. losing a Wicket) swings the match momentum.
* **Automated Analyst Notes:** Dynamic text summaries based on the current match state.

## 🛠️ Tech Stack
* **Frontend:** Streamlit, CSS
* **Machine Learning:** Scikit-Learn (Random Forest)
* **Data Processing:** Pandas, NumPy
* **Data Visualization:** Plotly Graph Objects

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ChiragKaushik4/ChiragKaushik_IPL_Analytics.git](https://github.com/ChiragKaushik4/ChiragKaushik_IPL_Analytics.git)
   cd ChiragKaushik_IPL_Analytics
Install the required dependencies:

Bash
pip install -r requirements.txt
Launch the Application:

Bash
streamlit run app.py
📊 Dataset
The model was trained on historical IPL ball-by-ball and match data, engineering key performance indicators like Current Run Rate (CRR), Required Run Rate (RRR), and Wickets in Hand.