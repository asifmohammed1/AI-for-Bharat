import joblib
import pandas as pd

model = joblib.load("model.pkl")

future_days = pd.DataFrame({"day": [8, 9, 10, 11, 12]})
predictions = model.predict(future_days)

for day, sales in zip(future_days["day"], predictions):
    print(f"📈 Day {day} → Predicted Sales: {int(sales)}")
