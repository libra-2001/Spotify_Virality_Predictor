import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- 1. Load the Model and Scaler ---
# These files must be in the same folder as app.py
try:
    model = joblib.load('final_viral_model.joblib')
    scaler = joblib.load('fitted_scaler.joblib')
except FileNotFoundError:
    st.error("Error: Model or Scaler files not found. Ensure 'final_viral_model.joblib' and 'fitted_scaler.joblib' are in the same folder as app.py.")
    st.stop()

# --- 2. Application Setup ---
st.set_page_config(page_title="Music Virality Predictor MVP", layout="centered")

st.title("🎧 High Potential Track Predictor (MVP)")

st.markdown("""
Welcome to the Minimum Viable Product for predicting a track's virality based on its audio features.
Our model identified key differentiators in high-potential tracks:
* **Tempo:** Tends to be slightly **faster** than the average hit song.
* **Loudness:** Tends to be slightly **quieter** or more dynamic than the average.
""")
# --- 3. Feature Input Sliders (14 Features) ---
st.header("Input Features")

col1, col2, col3 = st.columns(3)

with col1:
    artist_pop = st.slider('Artist Popularity', 0, 100, 50)
    followers = st.number_input('Followers', min_value=0, value=10000)
    acousticness = st.slider('Acousticness', 0.0, 1.0, 0.5)
    danceability = st.slider('Danceability', 0.0, 1.0, 0.7)
    energy = st.slider('Energy', 0.0, 1.0, 0.7)

with col2:
    instrumentalness = st.slider('Instrumentalness', 0.0, 1.0, 0.1)
    music_key = st.selectbox('Music Key', list(range(12)), help="0=C, 1=C#, etc.")
    liveness = st.slider('Liveness', 0.0, 1.0, 0.2)
    loudness = st.slider('Loudness (dB)', -60.0, 0.0, -8.0)
    mode = st.radio('Mode', [0, 1], help="0=Minor, 1=Major")

with col3:
    speechiness = st.slider('Speechiness', 0.0, 1.0, 0.1)
    tempo = st.slider('Tempo (BPM)', 50.0, 200.0, 120.0)
    valence = st.slider('Valence', 0.0, 1.0, 0.5)
    viral_prob = st.slider('Current Viral Prob', 0.0, 1.0, 0.5)

# --- 4. Prediction Logic ---

if st.button('Predict Virality Potential', type="primary"):
    
    # These 11 features must be in the EXACT order your model saw them
    # Based on your previous list, this is the most likely order:
    core_features = [
        acousticness, danceability, energy, instrumentalness, 
        music_key, liveness, loudness, mode, speechiness, 
        tempo, valence
    ]
    
    # Create DataFrame with the exact names the model expects
    input_df = pd.DataFrame([core_features], columns=[
        'acousticness', 'danceability', 'energy', 'instrumentalness', 
        'music_key', 'liveness', 'loudness', 'mode', 'speechiness', 
        'tempo', 'valence'
    ])
    
    try:
        # 1. Scale the data
        scaled_data = scaler.transform(input_df)
        
        # 2. Make the prediction
        probability = model.predict_proba(scaled_data)[0][1]
        
        st.divider()
        st.subheader(f"Prediction: {probability:.2%}")
        
        if probability > 0.7:
            st.balloons()
            st.success("🔥 This track has EXTREME viral potential!")
        elif probability > 0.5:
            st.info("📈 This track has moderate potential.")
        else:
            st.warning("🔈 This track has low viral potential.")
            
    except ValueError as e:
        # If the order is still slightly off, this will tell us the exact expected list
        st.error(f"Mapping Error: {e}")
