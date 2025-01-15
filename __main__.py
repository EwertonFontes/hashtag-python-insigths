import pandas as pd
import plotly.express as px

table = pd.read_csv("cancelamentos_sample.csv")
table = table.drop(columns="CustomerID")
print(table.info())
table = table.dropna()
print(table.info())

print(table["cancelou"].value_counts())
print(table["cancelou"].value_counts(normalize=True))
print(table["assinatura"].value_counts())


#graficos

#for column in table.columns:
#    graphic = px.histogram(table, x=column, color="cancelou", text_auto=True)
#    graphic.show()


#Duracao contrato -> diferente mensal
table = table[table["duracao_contrato"] != "Monthly"]

#ligacoes_callcenter -> menor  ou igual a 4
table = table[table["ligacoes_callcenter"] <= 4]

#atraso_pagementos < 20 dias
table = table[table["dias_atraso"] <= 20]

print(table["cancelou"].value_counts(normalize=True))



