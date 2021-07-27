import csv
import plotly_express as px
import pandas as pd
with open ("sleep.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()