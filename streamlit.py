import streamlit as st
import numpy     as np
import pandas    as pd

import plotly.express       as px
import plotly.graph_objects as go


# DATA
airbnb = pd.read_csv("data/airbnb.csv")


# STREAMLIT PAGE
st.set_page_config(layout="wide")

## HEADER
h1, h2 = st.columns((0.07, 1)) 

h1.image('images/airbnb.png', width = 100)
h2.title("Airbnb - New York")
h2.markdown("O código para este dashboard está disponível em: [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DinizMaths/airbnb-dashboard)")

st.markdown("Fundada em 2008 e com sede em San Francisco - Califórnia, o Airbnb é uma empresa americana que opera um mercado online para hospedagem. O Airbnb não é proprietário de nenhuma das propriedades listadas; em vez disso, obtém lucro ao receber comissão de cada reserva realizada.")

## TABS
tab1, tab2, tab3, tab4 = st.tabs(["DataFrame", "HistogramPlot", "MapPlot", "ViolinPlot"])

with tab1:
  st.dataframe(
    data=airbnb,
    width=1680
  )

with tab2:
  st.markdown("")

  categorias = airbnb["room_type"].unique()
  contagem   = airbnb["room_type"].value_counts()

  fig = go.Figure(data=[
    go.Bar(x=categorias, y=contagem)
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
  fig = go.Figure()

  fig.add_trace(go.Violin(
    y=airbnb["room_type"],
    x=airbnb["price"],
    fillcolor='lightseagreen',
    opacity=0.7,
    orientation='h'
  ))

  fig.update_layout(
    xaxis_title="Price",
    showlegend=False,
    width=1680
  )

  st.plotly_chart(fig)