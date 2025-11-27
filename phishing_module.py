import joblib
import pandas as pd
from url_feature_extractor import extract_numeric_features

# Load pipeline (must exist in same folder)
model = joblib.load("phishing_pipeline.pkl")

def predict_url(url):
    """
    Accept a single URL string, produce a DataFrame with the same columns
    used in training, and predict using the saved pipeline.
    """
    numeric = extract_numeric_features(url)
    df = pd.DataFrame([{"url": url, **numeric}])  # single-row DataFrame
    pred = model.predict(df)[0]
    # optionally get probability: proba = model.predict_proba(df)[0,1]
    return "🚨 Phishing Site Detected!" if pred == 1 else "✅ Safe URL"
