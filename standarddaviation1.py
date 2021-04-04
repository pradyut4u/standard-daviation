import csv
with open("sd1.csv", newline="")as f:
    reader=csv.reader(f)
    filedata= list(reader)

filedata.pop(0)
total=0
n=len(filedata)

for marks in filedata:
    total=total+float(marks[1])
    
mean=total/n
print("Mean is "+str(mean))

import pandas as pd
import plotly.express as pe

df=pd.read_csv("sd1.csv")
diagram=pe.scatter(df,x='Student number',y='Marks')
diagram.update_layout(shapes=[dict(
    type='line',y0=mean,y1=mean,x0=0,x1=n
)])
diagram.update_yaxes(rangemode="tozero")
diagram.show()