# phishing_module.py

import joblib

MODEL_PATH = "phishing_pipeline.pkl"
model = joblib.load(MODEL_PATH)

def predict_url(url: str, threshold: float = 0.5) -> str:
    """
    Use the TF-IDF + LogisticRegression pipeline to classify a URL.

    threshold: probability above which we call it phishing.
    """
    url = url.strip()
    if not url:
        return "⚠️ Please enter a URL."

    # model expects a list of texts
    proba = model.predict_proba([url])[0][1]  # probability of class 1 (phishing)
    pred = 1 if proba >= threshold else 0

    if pred == 1:
        return f"🚨 Phishing Site Detected! (phish_prob={proba:.2f})"
    else:
        return f"✅ Likely Safe URL (phish_prob={proba:.2f})"

