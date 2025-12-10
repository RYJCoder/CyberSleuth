# 🕵️‍♀️ CyberSleuth – Phishing & T&C Analyzer

**Live demo:** [CyberSleuth Web App](https://cybersleuth-se2bevjhjw4br8t9yzlzwk.streamlit.app/)

---

## 🚀 What is CyberSleuth?

CyberSleuth is a web-based cybersecurity tool that helps you quickly check if a URL is suspicious (possible phishing) using a machine-learning model — and also analyze pasted Terms & Conditions text for possible privacy/permission concerns.  

It’s a simple, user-friendly one-stop tool for quick security sanity checks.  

---

## 🧰 Features

- 🔍 **URL Phishing Detector** — provide a URL and the app returns a risk score and a warning if it thinks it’s phishing.  
- 📄 **T&C Analyzer** — paste Terms & Conditions text and get a summary & simple privacy/permission insights.  
- 📊 **Real-time ML model** — uses a trained pipeline (TF-IDF + classifier) to make predictions instantly.  
- ✅ **On-the-fly & easy to use** — no installs needed, just a browser; also easy to run locally if needed.  
- 🛠️ **Open-source & extendable** — all code is in this GitHub repo.

---

## 📚 How It Works (Model Overview)

- Model: TF-IDF vectorization of the URL string → Logistic Regression classifier.  
- Training: Balanced dataset with both phishing & benign URLs; oversampled real-world benign domains (e.g. google.com, github.com) so the model learns what safe sites “look like.”  
- Prediction: When you input a URL, the app transforms it with the trained pipeline and outputs a probability (`phish_prob`) + a verdict (Safe / Phishing).  

Result: a lightweight, real-time phishing detector — ideal for quick checks or integration into larger systems.

---

## 🧑‍💻 Run Locally (Development / Testing)

1. Clone the repo:
   ```bash
   git clone https://github.com/RYJCoder/CyberSleuth.git
   cd CyberSleuth

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. (Only if you want to retrain the model)
   ```bash
   python3 train_phishing_model.py

5. Run the webapp:
   ```bash
   streamlit run app.py
