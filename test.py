import pandas as pd


data = pd.read_csv("data/clients.csv")

data.to_excel("data/clients.xlsx")

