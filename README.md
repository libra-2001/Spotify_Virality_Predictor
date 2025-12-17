# 🎵 Spotify Virality Predictor MVP

A Machine Learning-powered web application that predicts whether a song has the potential to go viral based on its audio characteristics. 

## 📊 Project Overview
This project uses a Random Forest model and Streamlit to predict a song's viral potential based on 11 key audio features (energy, tempo, danceability, etc.). Built with Python, Scikit-Learn, and SQL, it bridges the gap between raw data analysis and interactive user deployment.

## 🚀 Features
* **Interactive Prediction**: Input song characteristics via a Streamlit sidebar to get real-time results.
* **ML Powered**: Utilizes a trained Random Forest Classifier to identify patterns in viral hits.
* **Data-Driven**: Trained on a dataset of Spotify tracks, exploring the relationship between technical audio traits and popularity.

## 🛠️ Technical Stack
* **Language:** Python
* **Libraries:** Pandas, Scikit-Learn, Streamlit, Joblib
* **Database:** PostgreSQL (Data source)
* **Visualization:** Power BI (Upcoming integration)

## 📋 The 11 Audio Features
The model evaluates the following traits:
1. Danceability 
2. Energy 
3. Loudness 
4. Speechiness 
5. Acousticness 
6. Instrumentalness 
7. Liveness 
8. Valence 
9. Tempo 
10. Duration (ms) 
11. Artist Followers

## ⚙️ How to Run Locally
1. Clone this repository.
2. Ensure you have the `.joblib` model files in the same directory.
3. Install requirements: `pip install streamlit pandas scikit-learn`
4. Launch the app: `streamlit run app.py`

---
*Developed as a Machine Learning MVP showcase.*
