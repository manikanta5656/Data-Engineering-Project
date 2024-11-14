import pandas as pd
import sqlalchemy as sal

# Database connection details
username = 'root'
password = 'Mani%405656'
host = 'localhost'
database = 'msql'

# Create SQLAlchemy engine for MySQL connection
engine =sal.create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')

# Define a sample DataFrame (replace this with your actual DataFrame)
df = pd.read_csv(r'C:\Users\mm2120\PycharmProjects\myproject\Codes\Dev\orders.csv')

# Connect to the MySQL database and insert the DataFrame
with engine.connect() as conn:
    df.to_sql('df_orderss', con=conn, index=False, if_exists='replace')
    print("fdsdfghj")

    # Verify the connection with a test query
    # result = conn.execute("SELECT * from df_orders")
    # print(result.fetchone())
