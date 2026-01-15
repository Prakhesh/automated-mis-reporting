import pandas as pd
from db.mysql_connection import get_connection

def fetch_sales_data():
    conn = get_connection()
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    print(fetch_sales_data())
