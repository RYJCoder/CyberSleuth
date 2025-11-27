# 🕵️‍♀️ CyberSleuth

A cybersecurity tool that detects phishing URLs using Machine Learning
(Random Forest + TF-IDF + numeric URL features) and analyzes Terms &
Conditions for privacy warnings.

## Features

- 🔍 Phishing URL Detector
- 📜 T&C Privacy Analyzer
- 🧠 ML Model trained on malicious_phish dataset
- 🚀 Streamlit Web App

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 train_phishing_model.py
streamlit run app.py
