import streamlit as st
import numpy     as np
import pandas    as pd

import plotly.express       as px
import plotly.graph_objects as go

import joblib
from sklearn.preprocessing import LabelEncoder


# DATA
airbnb = pd.read_csv("data/airbnb.csv")

# MODEL
model = joblib.load('random_forest_model.pkl')

neighbourhood_group_labels  = list(airbnb["neighbourhood_group"].unique())
neighbourhood_group_encoder = LabelEncoder()
neighbourhood_group_numbers = neighbourhood_group_encoder.fit_transform(neighbourhood_group_labels)

neighbourhood_labels  = list(airbnb["neighbourhood"].unique())
neighbourhood_encoder = LabelEncoder()
neighbourhood_numbers = neighbourhood_encoder.fit_transform(neighbourhood_labels)

room_type_labels  = list(airbnb["room_type"].unique())
room_type_encoder = LabelEncoder()
room_type_numbers = room_type_encoder.fit_transform(room_type_labels)

neighbourhood_group_encoder_dict = dict(zip(neighbourhood_group_labels, neighbourhood_group_numbers))
neighbourhood_encoder_dict = dict(zip(neighbourhood_labels, neighbourhood_numbers))
room_type_encoder_dict = dict(zip(room_type_labels, room_type_numbers))

# STREAMLIT PAGE
st.set_page_config(layout="wide")

## HEADER
h1, h2 = st.columns((0.07, 1)) 

h1.image('images/airbnb.png', width = 100)
h2.title("Airbnb - New York")
h2.markdown("O código para este dashboard está disponível em: [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DinizMaths/airbnb-dashboard)")

st.markdown("Fundada em 2008 e com sede em San Francisco - Califórnia, o Airbnb é uma empresa americana que opera um mercado online para hospedagem. O Airbnb não é proprietário de nenhuma das propriedades listadas, o lucro é obtido ao receber comissão de cada reserva realizada.")

## TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["DataFrame", "HistogramPlot", "MapPlot", "ViolinPlot", "Predict"])

with tab1:
  st.markdown("Abaixo se encontra o dataframe utilizado para a analise")

  st.dataframe(
    data=airbnb,
    width=1680
  )

with tab2:
  st.markdown("Abaixo é possível observar as distribuições com relação ao tipo de quarto ofertado")

  categories = airbnb["room_type"].unique()
  count      = airbnb["room_type"].value_counts()

  fig = go.Figure(data=[
    go.Bar(x=categories, y=count, marker=dict(color="#F05B61"))
  ])

  fig.update_layout(
    xaxis_title='',
    yaxis_title='Count',
    font=dict(size=14),
    showlegend=False,
    width=1680
  )

  st.plotly_chart(fig)

with tab3:
  st.markdown("Abaixo é possível observar como os dados estão distribuidos com relação ao bairro. O tamanho dos circulo que representa o dado está relacionado com o valor a ser pago pelo airbnb.")

  fig = px.scatter_mapbox(
    airbnb,
    lon=airbnb["longitude"],
    lat=airbnb["latitude"],
    size=airbnb["price"],
    color=airbnb["neighbourhood_group"],
    zoom=9,
  )

  fig.update_layout(
    legend_title_text="Neighbourhood Group",
    legend=dict(x=0, y=1),
    mapbox_style="carto-darkmatter",
    margin=dict(l=0, r=0, t=0, b=0),
    width=1680
  )

  st.plotly_chart(fig)

with tab4:
  st.markdown("Abixo é mostrada uma comparação entre os tipos de quartos e o preço a partir do gráfico de violino")

  fig = go.Figure()

  fig.add_trace(go.Violin(
    y=airbnb["room_type"],
    x=airbnb["price"],
    fillcolor='#F05B61',
    opacity=1,
    orientation='h',
    marker=dict(color="#D0555A")
  ))

  fig.update_layout(
    xaxis_title="Price",
    showlegend=False,
    width=1680
  )

  st.plotly_chart(fig)

with tab5:
  st.markdown("Abixo é mostrada uma comparação entre os tipos de quartos e o preço a partir do gráfico de violino")

  col1, col2, col3, col4 = st.columns(4)

  with col1:
    feature1 = st.selectbox("neighbourhood_group", list(airbnb["neighbourhood_group"].unique()))
  with col2:
    feature2 = st.selectbox("neighbourhood", list(airbnb["neighbourhood"].unique()))
  with col3:
    feature3 = st.selectbox("room_type", list(airbnb["room_type"].unique()))
  with col4:
    feature4 = st.number_input("minimum_nights", value=1, step=1, min_value=1)

  if st.button('Predict Price'):
    new_data = pd.DataFrame([[neighbourhood_group_encoder_dict[feature1], neighbourhood_encoder_dict[feature2], room_type_encoder_dict[feature3], feature4]], columns=["neighbourhood_group", "neighbourhood", "room_type", "minimum_nights"])
    pred = model.predict(new_data)

    st.markdown(f"### Valor Predito: ${pred[0]:.2f}")