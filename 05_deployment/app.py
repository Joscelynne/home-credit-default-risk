# 05_deployment/app.py


from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('../artifacts/home_credit_model.joblib')

@app.post("/evaluate_risk")
def evaluate_risk(data: dict):
    df = pd.DataFrame([data])
    prob = model.predict_proba(df)[0][1]

    decision = (
        "APROBAR" if prob < 0.3 else
        "REVISIÓN MANUAL" if prob < 0.6 else
        "RECHAZAR"
    )

    return {
        "prob_default": float(prob),
        "decision": decision
    }
