import pandas as pd
import os

tabela = pd.DataFrame()
pasta = "./Vendas"

lista_arquivos = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith(".csv")]

dfs = []

for arquivo in lista_arquivos:
    caminho_arquivo = os.path.join(pasta, arquivo)
    df = pd.read_csv(caminho_arquivo)
    dfs.append(df)

tabela = pd.concat(dfs, ignore_index=True)

tabela_total = tabela

tabela_produto = tabela_total.groupby("Produto").sum()
print(tabela_produto)

tabela_total["Faturamento"] = (
    tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
)
tabela_faturamento = tabela_total.groupby("Produto").sum()

print(tabela_faturamento)

tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Quantidade Vendida", "Faturamento"]]
print(tabela_lojas)

import plotly.express as px

grafico_faturamento = px.bar(
    tabela_faturamento, x=tabela_faturamento.index, y="Faturamento")
grafico_faturamento.show()

grafico_loja = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")
grafico_loja.show()
