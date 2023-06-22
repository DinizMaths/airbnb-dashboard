import streamlit as st
import numpy     as np
import pandas    as pd

import plotly.express as px


# DATA
airbnb = pd.read_csv("data/airbnb.csv")


# STREAMLIT PAGE
st.set_page_config(layout="wide")

t1, t2 = st.columns((0.07, 1)) 

t1.image('images/airbnb.png', width = 100)
t2.title("Airbnb - New York")
t2.markdown("O código para este dashboard está disponível em: [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DinizMaths/airbnb-dashboard)")


see_data = st.expander("Clique para ver os dados 👉")

with see_data:
  st.dataframe(data=airbnb)