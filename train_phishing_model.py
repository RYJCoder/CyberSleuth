# train_phishing_model.py
#
# Balanced TF-IDF + LogisticRegression model
# with strong extra benign examples for real-world domains.

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

print("🚀 Starting training script...")

# 1) Load dataset
df = pd.read_csv("malicious_phish.csv")
print("📄 Columns:", df.columns)
print("🔍 Types:", df["type"].unique())

# 2) Keep only phishing and benign
df = df[df["type"].isin(["phishing", "benign"])].reset_index(drop=True)
print("\nCounts before balancing:")
print(df["type"].value_counts())

# 3) Binary label: phishing = 1, benign = 0
df["label"] = df["type"].apply(lambda x: 1 if x == "phishing" else 0)

# 4) Split phishing and benign
phish = df[df["label"] == 1]
benign = df[df["label"] == 0]

# 5) Balance classes (use same count from each, up to 40k)
n = min(len(phish), len(benign), 40000)
phish_bal = phish.sample(n=n, random_state=42)
benign_bal = benign.sample(n=n, random_state=42)

df_bal = pd.concat([phish_bal, benign_bal], ignore_index=True)

# 6) Add MANY extra real-world benign URLs (oversampled)
extra_benign_urls = [
    "https://google.com",
    "https://www.google.com",
    "https://github.com",
    "https://www.github.com",
    "https://wikipedia.org",
    "https://www.wikipedia.org",
    "https://stackoverflow.com",
    "https://www.stackoverflow.com",
    "https://microsoft.com",
    "https://www.microsoft.com",
    "https://apple.com",
    "https://www.apple.com",
    "https://amazon.com",
    "https://www.amazon.com",
]

# Repeat each URL, e.g. 200 times, to strongly influence the model
multiplier = 200
extra_urls_repeated = extra_benign_urls * multiplier

extra_df = pd.DataFrame({
    "url": extra_urls_repeated,
    "label": [0] * len(extra_urls_repeated),
    "type": ["benign"] * len(extra_urls_repeated),
})

df_bal = pd.concat([df_bal, extra_df], ignore_index=True)

print("\nCounts after balancing + extra benign:")
print(df_bal["label"].value_counts())

# 7) Features and labels
X = df_bal["url"].astype(str)
y = df_bal["label"]

# 8) Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 9) Pipeline: TF-IDF + Logistic Regression
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        max_features=1000,     # a bit more features, still manageable
        ngram_range=(1, 2),
        min_df=5
    )),
    ("clf", LogisticRegression(
        max_iter=1000
    )),
])

print("\n⏳ Training model...")
pipeline.fit(X_train, y_train)
print("✅ Training completed.")

# 10) Evaluate
y_pred = pipeline.predict(X_test)
print("\n📊 Confusion matrix:")
print(confusion_matrix(y_test, y_pred))
print("\n📋 Classification report:")
print(classification_report(y_test, y_pred))

# 11) Save pipeline
joblib.dump(pipeline, "phishing_pipeline.pkl")
print("\n✅ Saved phishing_pipeline.pkl")
