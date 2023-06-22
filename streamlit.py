import streamlit as st
import numpy     as np
import pandas    as pd


# DATA
airbnb = pd.read_csv("data/airbnb.csv")


# STREAMLIT PAGE
st.set_page_config(layout="wide")
st.title("Airbnb - New York")

st.markdown("")
st.markdown("O código para este dashboard está disponível em: ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)")
st.markdown("If you are interested in how this app was developed check out my [Medium article](https://tim-denzler.medium.com/is-bayern-m%C3%BCnchen-the-laziest-team-in-the-german-bundesliga-770cfbd989c7)")
    

st.markdown("")
see_data = st.expander("Clique para ver os dados 👉")

with see_data:
  st.dataframe(data=airbnb)