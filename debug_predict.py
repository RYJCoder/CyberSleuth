# debug_predict.py
import joblib
import pandas as pd
from url_feature_extractor import extract_numeric_features

model = joblib.load("phishing_pipeline.pkl")

url = "https://google.com"
numeric = extract_numeric_features(url)
df = pd.DataFrame([{"url": url, **numeric}])

print("Input features:", df.to_dict(orient="records")[0])
proba = model.predict_proba(df)[0]    # [prob_not_phish, prob_phish]
pred = model.predict(df)[0]
print("predict:", pred, "prob_phish:", proba[1])
