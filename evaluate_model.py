# evaluate_model.py
import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
from sklearn.model_selection import train_test_split
from url_feature_extractor import get_feature_dataframe

# 1. Load dataset
df = pd.read_csv("malicious_phish.csv")

# Keep only phishing vs benign
df = df[df["type"].isin(["phishing", "benign"])].reset_index(drop=True)
df["label"] = df["type"].apply(lambda x: 1 if x == "phishing" else 0)

# 2. Create combined features
numeric_df = get_feature_dataframe(df["url"].astype(str))
combined = pd.concat([df["url"].astype(str).rename("url"), numeric_df], axis=1)

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(
    combined, df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

# 4. Load trained pipeline
model = joblib.load("phishing_pipeline.pkl")

# 5. Predict
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred))
print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification report:\n", classification_report(y_test, y_pred))
