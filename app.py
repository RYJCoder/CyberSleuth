# app.py

import streamlit as st
from phishing_module import predict_url
from tnc_module import summarize_tnc, extract_info

st.set_page_config(page_title="CyberSleuth", layout="centered")
st.title("🕵️‍♀️ CyberSleuth - Phishing & T&C Analyzer")

choice = st.sidebar.selectbox("Choose a Tool", ["Phishing Detector", "T&C Analyzer"])

if choice == "Phishing Detector":
    url = st.text_input("Enter URL to scan")
    if st.button("Check URL"):
        if not url.strip():
            st.warning("Please enter a URL.")
        else:
            result = predict_url(url.strip())
            st.write(result)

else:
    tnc_text = st.text_area("Paste Terms & Conditions here")
    if st.button("Analyze T&C"):
        summary = summarize_tnc(tnc_text)
        info = extract_info(tnc_text)
        st.subheader("Summary")
        st.write(summary)
        st.subheader("Privacy Insights")
        for i in info:
            st.write("- " + i)
