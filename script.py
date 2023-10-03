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

print(tabela)