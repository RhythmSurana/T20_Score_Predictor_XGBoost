import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Tanzania',
 'Samoa',
 'Singapore',
 'Nigeria',
 'Saudi Arabia',
 'Pakistan',
 'Malaysia',
 'Finland',
 'Hong Kong',
 'Rwanda',
 'Romania',
 'Sri Lanka',
 'Germany',
 'Zimbabwe',
 'Malawi',
 'Qatar',
 'Estonia',
 'Kenya',
 'Uganda',
 'Bangladesh',
 'Austria',
 'Bahrain',
 'United Arab Emirates']

cities = ['Kigali City', 'Singapore', 'Blantyre', 'Entebbe']

st.title("Cricket Score Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs Done (Works for >5)')
with col5:
    wickets = st.number_input('Wickets')

last_five = st.number_input('Runs scored in Last Five Overs')

if st.button('Predict Score'):
 balls_left = 120 - (overs * 6)
 wickets_left = 10 - wickets
 crr = current_score / overs

 input_df = pd.DataFrame(
  {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city, 'current_score': [current_score],
   'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five], 'last_30_runs': [last_five] })
 result = pipe.predict(input_df)
 st.header("Predicted Score - " + str(int(result[0])))
