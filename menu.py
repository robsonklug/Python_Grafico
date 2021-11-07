import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


tabela_produto = pd.read_excel("planilha_producao_2021.xlsx")
#print(tabela_produto)


producao_dia = tabela_produto.groupby(["Produto","Data"]).sum()

#print(producao_dia)
producao_dia.plot(kind='bar') 
plt.show()

