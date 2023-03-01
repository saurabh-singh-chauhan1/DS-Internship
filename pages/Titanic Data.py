import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import seaborn as sns

st.title("Dashborad for Titanic Dataset")


FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

classes = st.selectbox("Select the class:", df['class'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['class'] == classes], x="age")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['class'] == classes], y="age")
col2.plotly_chart(fig_2, use_container_width=True)