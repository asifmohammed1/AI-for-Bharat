from flask import Flask, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/forecast/<int:day>")
def forecast(day):
    prediction = model.predict([[day]])
    return jsonify({
        "day": day,
        "predicted_sales": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
