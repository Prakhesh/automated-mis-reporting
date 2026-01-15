from etl.fetch_data import fetch_sales_data

def generate_mis():
    df = fetch_sales_data()
    report = df.groupby("region")["amount"].sum()
    print("MIS REPORT:")
    print(report)

if __name__ == "__main__":
    generate_mis()
