# train_phishing_model.py
"""
Train a pipeline that combines TF-IDF (on the 'url' column)
with numeric URL features (from url_feature_extractor),
then saves the pipeline to phishing_pipeline.pkl
"""

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from url_feature_extractor import get_feature_dataframe

print("🚀 Starting training script...")

# --- 1) Load dataset ---
df = pd.read_csv("malicious_phish.csv")
print(f"📄 Columns: {df.columns}")
print(f"🔍 Types: {df['type'].unique()}")

# Optional: reduce dataset for fast testing (uncomment to use)
# df = df.sample(n=5000, random_state=42)

# --- 2) Make binary label (phishing=1, everything else=0) ---
df["label"] = df["type"].apply(lambda x: 1 if x == "phishing" else 0)

# Keep only phishing vs benign if you want strict labels (optional)
# df = df[df["type"].isin(["phishing", "benign"])].reset_index(drop=True)

# --- 3) Build combined DataFrame: 'url' + numeric features ---
url_series = df["url"].astype(str)
numeric_df = get_feature_dataframe(url_series)
combined = pd.concat([url_series.reset_index(drop=True).rename("url"), numeric_df.reset_index(drop=True)], axis=1)

# --- 4) Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(combined, df["label"], test_size=0.2, random_state=42, stratify=df["label"])

# --- 5) Preprocessor: TF-IDF on 'url', pass numeric columns through ---
# ColumnTransformer uses column names when X is a DataFrame
preprocessor = ColumnTransformer(
    transformers=[
        ("tfidf", TfidfVectorizer(max_features=500), "url"),
    ],
    remainder="passthrough"  # keep numeric columns as-is
)

# --- 6) Full pipeline (preprocessor + classifier) ---
clf = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))
])

# --- 7) Fit and save ---
print("⏳ Training (this may take some time)...")
clf.fit(X_train, y_train)
print("✅ Training completed.")

joblib.dump(clf, "phishing_pipeline.pkl")
print("✅ Pipeline saved to phishing_pipeline.pkl")
