import pandas as pd
import plotly.express as pe

df=pd.read_csv("sd.csv")
diagram=pe.scatter(df,x='Student Number',y='Marks')
diagram.show()