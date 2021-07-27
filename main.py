import csv
import numpy as np
import plotly_express as px
def plot(data):
    with open ("marks.csv") as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def getDataSource(path):
    temp=[]
    icream=[]
    with open(path) as f:
        df=csv.DictReader(f)
        for row in df:
            temp.append(float(row["Days Present"]))
            icream.append(float(row["Marks In Percentage"]))

    return{"x":temp,"y":icream}

def findcorrelation(ds):
    correlation=np.corrcoef(ds["x"],ds["y"])
    print(correlation[0,1])

def main():
    data="marks.csv"
    ds=getDataSource(data)
    findcorrelation(ds)
    plot(data)

main()
