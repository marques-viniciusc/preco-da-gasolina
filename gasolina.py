import pandas as pd
import seaborn as sns

df = pd.read_csv('gasolina.csv', sep=',')
grafico = sns.lineplot(x='dia', y='venda', data=df)
grafico.get_figure().savefig('grafico_gasolina.png')