import pandas as pd
df = pd.read_csv('cars.csv')
a = df.iloc[:5,1:11:2]
b = df[df['Model']=='Mazda RX4']
c = df.loc[df['Model']=='Camaro Z28',['cyl']]
d = df.loc[[1,28,18],['cyl','gear']]