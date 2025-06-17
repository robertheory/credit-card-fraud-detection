
import numpy as np
from schemas.predict import PredictSchema
import pickle
import os
import pandas as pd


def load_model(model_filename='credit_card_fraud_model.pkl'):
    """Carrega o modelo de ML usando pickle."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', 'ml', model_filename)
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found")
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
        model_file.close()
    return model


def format_input_data(predict_data: PredictSchema):
    """
    Converte dados do PredictSchema para o formato de entrada do modelo.
    Retorna um array numpy 2D, pronto para ser usado no scaler/modelo.
    """
    atributos = [
        'distance_from_home',
        'distance_from_last_transaction',
        'ratio_to_median_purchase_price',
        'repeat_retailer',
        'used_chip',
        'used_pin_number',
        'online_order'
    ]
    # Cria DataFrame para garantir ordem dos atributos
    df = pd.DataFrame([{attr: getattr(predict_data, attr)
                      for attr in atributos}], columns=atributos)
    return df.values.astype(float)
