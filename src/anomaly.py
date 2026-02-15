import pandas as pd

df = pd.read_csv("data/sales.csv")

mean_sales = df["sales"].mean()
std_sales = df["sales"].std()

df["anomaly"] = df["sales"].apply(
    lambda x: "⚠️ Anomaly" if abs(x - mean_sales) > 2 * std_sales else "Normal"
)

print(df[["date", "sales", "anomaly"]])
