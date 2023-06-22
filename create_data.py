import pandas as pd


new_york_airbnb = pd.read_csv("https://raw.githubusercontent.com/DinizMaths/DCA-ciencia-de-dados/main/Unidade-1/data/AB_NYC_2019.csv")

new_york_airbnb = new_york_airbnb.query("price > 0")
new_york_airbnb = new_york_airbnb.query("availability_365 > 0")

new_york_airbnb.to_csv("data/airbnb.csv", index=False)