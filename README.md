# 🏏 IPL Match Intelligence & Prediction Engine

<p align="center">
  <b>Real-Time IPL Win Probability • Tactical Analytics • Momentum Simulation</b>
</p>

<p align="center">
  A Machine Learning powered sports analytics dashboard built with Python, Streamlit and Scikit-Learn.
</p>

---

## 📌 Project Overview

The **IPL Match Intelligence & Prediction Engine** is an enterprise-style, real-time Machine Learning dashboard designed to predict the **win probability of a chasing team** during an IPL match.

The application transforms live match telemetry into actionable sports analytics using a trained **Random Forest Classifier**, interactive visualizations, tactical pressure analysis, and what-if simulations.

---

## 🚀 Key Features

### 🎯 Real-Time Win Probability

Powered by a trained **Random Forest Classifier**, the system estimates the chasing team's probability of winning based on the current match situation.

Key inputs include:

- Current Score
- Target Score
- Runs Remaining
- Balls Remaining
- Wickets Lost
- Current Run Rate (CRR)
- Required Run Rate (RRR)
- Wickets in Hand

---

### 📊 Tactical Pressure Index

An interactive **XAI-inspired radar chart** that visualizes the pressure created by different match conditions.

The Tactical Pressure Index considers:

- Required Run Rate
- Wickets Lost
- Target Load
- Current Match Situation

This provides a quick visual representation of how difficult the current chase is.

---

### 🔮 Momentum Simulator

A **What-If sensitivity analysis engine** that calculates how different outcomes on the next delivery could potentially change the predicted win probability.

Example scenarios:

- 🏏 Six
- 🏏 Four
- 🟢 Single
- ⚪ Dot Ball
- 🔴 Wicket

The system recalculates the match state for each scenario and displays the potential change in momentum.

---

### 🧠 Automated Analyst Notes

The dashboard automatically generates contextual match analysis based on the current match state.

Examples include:

- High required run rate
- Pressure due to wickets lost
- Comfortable chase
- Increasing run-rate pressure
- Strong position with wickets in hand
- Potential momentum shift

---

### 📺 Broadcast-Style Dashboard

The application uses a modern sports-broadcast-inspired UI with:

- Real-time match metrics
- Win probability indicators
- Interactive charts
- Tactical pressure visualization
- Momentum simulation
- Automated analyst commentary
- Custom CSS styling

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core development |
| 🎈 **Streamlit** | Interactive web dashboard |
| 🤖 **Scikit-Learn** | Machine Learning |
| 🌲 **Random Forest** | Win probability prediction |
| 🐼 **Pandas** | Data processing |
| 🔢 **NumPy** | Numerical computation |
| 📊 **Plotly Graph Objects** | Interactive visualizations |
| 🎨 **CSS** | Custom dashboard styling |

---

# 💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/ChiragKaushik4/ChiragKaushik_IPL_Analytics.git
````

### 2. Navigate to the Project

```bash
cd ChiragKaushik_IPL_Analytics
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Application

```bash
streamlit run app.py
```

The Streamlit application will start locally and provide a URL in the terminal.

---

# 📦 Requirements

The project dependencies are listed in:

```text
requirements.txt
```

Main libraries include:

```text
streamlit
pandas
numpy
scikit-learn
plotly
```

---

# 🧠 Machine Learning

The prediction engine uses a **Random Forest Classifier** trained on historical IPL match data.

The model analyzes the current state of a chase and produces a probability-based prediction.

### Important Features

* Current Score
* Target Score
* Runs Remaining
* Balls Remaining
* Wickets Lost
* Wickets in Hand
* Current Run Rate (CRR)
* Required Run Rate (RRR)
* Target Load

The trained ML pipeline is stored in:

```text
pipe.pkl
```

---

# 📊 Dataset

The model was trained using the **IPL Complete Dataset**, containing historical IPL match and ball-by-ball data.

🔗 **Dataset:** [IPL Complete Dataset (2008–2024)](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)

The dataset was used for data preprocessing, feature engineering, and training the Machine Learning model.

Feature engineering was performed to generate important match-state indicators such as:

* **Current Run Rate (CRR)**
* **Required Run Rate (RRR)**
* **Runs Remaining**
* **Balls Remaining**
* **Wickets in Hand**
* **Wickets Lost**
* **Target Load**

These engineered features allow the model to evaluate the match dynamically instead of relying only on the current score.

---

# 🔬 How It Works

```text
             Historical IPL Data
                     │
                     ▼
          Data Cleaning & Processing
                     │
                     ▼
             Feature Engineering
                     │
                     ▼
          Random Forest Classifier
                     │
                     ▼
             Live Match Inputs
                     │
                     ▼
          Win Probability Prediction
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
 Tactical Pressure       Momentum Simulator
     Analysis                 │
          │                   ▼
          └──────────► Analyst Insights
```

---

# 🔮 Momentum Simulation

The Momentum Simulator creates hypothetical match states for possible next-ball outcomes.

For example:

```text
Current Match State
        │
        ├── Six
        │
        ├── Four
        │
        ├── Single
        │
        ├── Dot Ball
        │
        └── Wicket
              │
              ▼
      Recalculate Match State
              │
              ▼
      Run Through ML Pipeline
              │
              ▼
      Compare Win Probabilities
```

This allows users to understand how individual events can affect the predicted match situation.

---

# 📂 Project Structure

```text
ChiragKaushik_IPL_Analytics/
│
├── app.py
├── pipe.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── ...
│
└── assets/
    └── ...
```

---

# 🎯 Project Objective

The objective of this project is to demonstrate how **Machine Learning, feature engineering, and real-time analytics** can be applied to cricket.

Instead of displaying only traditional scorecard statistics, the system converts match data into:

* Predictive insights
* Tactical analytics
* Win probability
* Momentum analysis
* Interactive visualizations
* Automated match commentary

---

# 📈 Future Improvements

Potential future improvements include:

* [ ] Live IPL API integration
* [ ] Real-time ball-by-ball data
* [ ] Player-level performance features
* [ ] Venue-specific analysis
* [ ] Batter vs Bowler matchup analysis
* [ ] Team strength indicators
* [ ] Advanced XAI using SHAP
* [ ] Historical prediction accuracy dashboard
* [ ] Model comparison with XGBoost / LightGBM
* [ ] Deployment using Streamlit Cloud
* [ ] Mobile-friendly UI

---

# ⚠️ Disclaimer

The win probability displayed by this application is a **Machine Learning estimate** based on historical data and engineered match-state features.

It is not a guarantee of the actual match outcome.

Model performance depends on the quality of the training data, feature engineering, and model configuration.

---

# 👨‍💻 Author

## Chirag Kaushik

**B.Tech CSE | Machine Learning & Data Science Enthusiast**

🔗 **GitHub:**
https://github.com/ChiragKaushik4

---

<p align="center">
  ⭐ If you found this project interesting, consider giving the repository a star!
</p>
```
