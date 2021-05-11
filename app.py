#!/usr/bin/env python
# coding: utf-8


import parselmouth
import numpy as np
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.markdown('# How Analysis Parameters Affect Pitch Measures in Praat')

# Load sound into Praat
sound = parselmouth.Sound("03-01-01-01-01-01-01.wav")

audio_file = open('03-01-01-01-01-01-01.wav', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/wav')

st.sidebar.markdown("## Praat's Pitch Floor and Ceiling Settings")
floor = st.sidebar.slider('Pitch Floor', 50, 250, 75)
ceiling = st.sidebar.slider('Pitch Ceiling', 300, 700, 600)
kill_octave_jumps = st.sidebar.checkbox("Kill Octave Jumps")


pitch = sound.to_pitch(pitch_floor=floor, pitch_ceiling=ceiling)
if kill_octave_jumps:
    parselmouth.praat.call(pitch, "Kill octave jumps")

x = pitch.xs()
pitch_values = pitch.selected_array['frequency']
pitch_values[pitch_values==0] = np.nan
y = pitch_values
df = pd.DataFrame({"Time (s)": x,
                  "Frequency (Hz)":y})

st.markdown(f"# Mean Pitch: {round(df['Frequency (Hz)'].mean(), 3)}")
fig, ax = plt.subplots()
ax.plot(df['Time (s)'], df['Frequency (Hz)'], marker='o')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')
ax.grid(True)
st.pyplot(fig)

st.markdown(f"# Data")
st.markdown(f"## NaN's filtered out")
st.table(df.dropna())

st.text("""Sound from: Livingstone SR, Russo FA (2018) 
The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS):
A dynamic, multimodal set of facial and vocal expressions in North American English. 
PLoS ONE 13(5): e0196391. https://doi.org/10.1371/journal.pone.0196391.""")
