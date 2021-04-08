#!/usr/bin/env python
# coding: utf-8


import parselmouth
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_interactions import heatmap_slicer
import matplotlib as mpl
import streamlit as st 
import pandas as pd

st.markdown('# How Analysis Parameters Affect Pitch Measures in Praat')

# Load sound into Praat
sound = parselmouth.Sound("03-01-01-01-01-01-01.wav")
waveform = pd.DataFrame({"Amplitude": sound.values[0].T})
st.line_chart(waveform)


# Load sound into streamlit


audio_file = open('03-01-01-01-01-01-01.wav', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/wav')

st.markdown("## Praat's Pitch Floor and Ceiling Settings")
floor = st.slider('Pitch Floor', 50, 250, 75)
ceiling = st.slider('Pitch Ceiling', 300, 700, 600)
pitch = sound.to_pitch(pitch_floor=floor, pitch_ceiling=ceiling)
x = pitch.xs()
pitch_values = pitch.selected_array['frequency']
pitch_values[pitch_values==0] = np.nan
y = pitch_values
df = pd.DataFrame({"Frequency(Hz)":y})
st.line_chart(df)
