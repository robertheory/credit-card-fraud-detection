from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS
from schemas.predict import PredictSchema
from utils import load_model, format_input_data
import pickle
import numpy as np
import pandas as pd

# API Info
info = Info(
    title="Credit Card Fraud Detection API",
    version="1.0.0",
    description="API for detecting credit card fraud using machine learning",
)

# Initialize Flask app with OpenAPI
app = OpenAPI(__name__, info=info)
CORS(app)

# API Tags
home_tag = Tag(
    name="Docs",
    description="Documentation selection: Swagger, Redoc or ReDoc"
)


@app.get('/', tags=[home_tag])
def home():
    """Redirect to /openapi, screen that allows choosing the documentation style."""
    return redirect('/openapi/swagger')

    """Register stats routes."""


predict_tag = Tag(
    name="Predict",
    description="Endpoints for predicting credit card fraud using a machine learning model."
)


@app.post(
    '/predict',
    tags=[predict_tag],
    summary="Predict credit card fraud",
)
def predict(body: PredictSchema):
    """
    Predict credit card fraud based on input data.
    """

    # Load the model
    model = load_model('credit_card_fraud_model.pkl')

    # Prepare input data
    input_data = format_input_data(body)

    # Make prediction
    prediction = model.predict(input_data)
    print(f"Prediction: {prediction}")

    return {"isFraud": bool(prediction[0])}
