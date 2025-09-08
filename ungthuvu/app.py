from flask import Flask, request, jsonify, render_template
import joblib, pandas as pd

app = Flask(__name__)
model = joblib.load("rf_model.pkl")
FEATURES = ["concave points_mean","concave points_worst","area_worst","concavity_mean","radius_worst"]

@app.route("/")
def home():
    return render_template("index.html")  # hiển thị trang web

@app.post("/predict")
def predict():
    x = pd.DataFrame([request.json], columns=FEATURES)
    pred = int(model.predict(x)[0])
    proba = model.predict_proba(x)[0].tolist()
    return jsonify({"prediction": pred, "proba": proba})

if __name__ == "__main__":
    app.run(debug=True)
