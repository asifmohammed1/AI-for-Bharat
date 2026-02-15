import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data/sales.csv")
df["date"] = pd.to_datetime(df["date"])
df["day"] = df["date"].dt.day

X = df[["day"]]
y = df["sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")

print("✅ Demand Forecasting Model Trained & Saved")
