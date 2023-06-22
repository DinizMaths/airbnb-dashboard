import streamlit as st
import numpy     as np
import pandas    as pd


st.set_page_config(layout="wide")

airbnb = pd.read_csv("/data/airbnb.csv")