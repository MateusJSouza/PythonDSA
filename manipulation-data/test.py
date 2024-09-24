import pandas as pd

pd.__version__

arquivo = "salarios.csv"

df = pd.read_csv(arquivo)

df.head()