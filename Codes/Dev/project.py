import kaggle
import subprocess
import zipfile
import pandas
import os

import pandas as pd

#for i in file:
    #print(i)
#subprocess.run(["kaggle","datasets","download","ankitbansal06/retail-orders","-f","orders.csv"],check=True)
#zip_ruf = zipfile.ZipFile("orders.csv.zip")

#zip_ruf.extractall()
#zip_ruf.close()
df=pd.read_csv('orders.csv')
#To know the first five recods
#print(df.head(5))
#To know the columns in the dataset
#print(df.columns)
#curent_dir=os.getcwd()
#file=os.listdir(curent_dir)
#To know the dtypes of the dataset
#print(df.dtypes)
#To know the info,shape,descibe the dataset
#print(df.shape,df.info,df.describe(), end='/n')
# To convert the Order Date column datatype to datetime
#print(df['Order Date'].dtype)
df['Order Date']=pd.to_datetime(df['Order Date'],format="%Y-%m-%d")
#print(df['Order Date'].dtype)
#To covert some values in the column to Null values(nan)
df=pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
#To check the unique values in the specific column
#print(df['Ship Mode'].unique())
#To rename the specific colunm name you want
df.rename(columns={'Order Id':'order id','Order Date':'order date','City':'city'}, inplace=True)
#To convert all the columns into the lower string
df.columns=df.columns.str.lower()
#to replace space(' ') with the '_'
df.columns=df.columns.str.replace(' ','_')
# To dervie a new discount value
df['discount']=df['list_price']*df['discount_percent']*.01
#To derive the sale price
df['sale_price']=df['list_price']-df['discount']
#print(df['sale_price'])
#To derive the total profit
df['profit']=df['sale_price']-df['cost_price']
#print(df['profit'])
#To drop columns
df=df.drop(columns=['list_price','discount_percent','cost_price'])
print(df.columns)






