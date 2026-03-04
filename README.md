# 🏏 T20 Cricket Score Predictor

A Machine Learning powered web application that predicts the final score of a T20 cricket innings based on the current match situation.

Built using **Python, Scikit-Learn, XGBoost, and Streamlit**, this project takes live match inputs and estimates the projected total score using historical T20 match data.

## 🚀 Features

- Predicts final T20 score in real-time
- Interactive Streamlit web interface
- Trained on historical international T20 data
- Clean ML pipeline using Scikit-Learn
- Fast and lightweight deployment

## 📊 Input Parameters

The model makes predictions based on:

- 🏏 Batting Team  
- 🎯 Bowling Team  
- 🌍 Match City  
- 📈 Current Score  
- ⏱ Overs Completed  
- ❌ Wickets Fallen  
- 🔥 Runs Scored in Last 5 Overs  

## 🧠 Machine Learning Pipeline

The project includes:

- Data Cleaning & Feature Engineering  
- OneHot Encoding (Categorical Features)  
- Standard Scaling (Numerical Features)  
- Model Training using:
  - Random Forest Regressor
  - XGBoost Regressor
- Pipeline creation using `ColumnTransformer`
- Model serialization using `pickle`
- Deployment via Streamlit

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- XGBoost  
- Streamlit  

## 📂 Project Structure

.
├── data/                # Dataset files

├── pipe.pkl             # Trained ML pipeline

├── main.py              # Streamlit app

├── requirements.txt     # Project dependencies

└── README.md


## ▶️ Run Locally

1️⃣ Clone the repository

git clone <your-repo-link>
cd <repo-folder>


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run the Streamlit app

streamlit run main.py


## 📈 Future Improvements

- Add win probability prediction
- Improve model accuracy with advanced feature engineering
- Deploy to Streamlit Cloud / Render
- Add match visualization dashboard
- Integrate live match API


## 📌 Author

Built with ❤️ by Rhythm using Machine Learning and Streamlit.

Just tell me 👌
