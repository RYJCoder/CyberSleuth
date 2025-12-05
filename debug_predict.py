# debug_predict.py

import joblib

MODEL_PATH = "phishing_pipeline.pkl"
model = joblib.load(MODEL_PATH)

test_urls = [
    "https://google.com",
    "https://github.com",
    "https://wikipedia.org",
    "http://paypal-account-verify.com/login",
    "http://192.168.1.15/secure-login",
]

for url in test_urls:
    proba = model.predict_proba([url])[0][1]  # P(phishing)
    pred = model.predict([url])[0]
    print(f"URL: {url}")
    print(f"  predicted_label: {pred} (1=phish,0=benign)")
    print(f"  phishing_probability: {proba:.3f}")
    print()
