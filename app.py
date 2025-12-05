import streamlit as st
from phishing_module import predict_url
from tnc_module import summarize_tnc, extract_info

st.set_page_config(page_title="CyberSleuth")

st.title("🕵️‍♀️ CyberSleuth - Cybersecurity Analyzer")

choice = st.sidebar.selectbox("Choose a Tool", ["Phishing Detector", "T&C Analyzer"])

if choice == "Phishing Detector":
    url = st.text_input("Enter a URL:")
    threshold = st.slider("Phishing sensitivity (higher = stricter)", 0.1, 0.9, 0.5, 0.05)
    if st.button("Check URL"):
        result = predict_url(url, threshold=threshold)
        st.write(result)

elif choice == "T&C Analyzer":
    tnc_text = st.text_area("Paste Terms & Conditions:")
    if st.button("Analyze Text"):
        summary = summarize_tnc(tnc_text)
        insights = extract_info(tnc_text)

        st.subheader("Summary:")
        st.write(summary)

        st.subheader("Privacy Insights:")
        for item in insights:
            st.write("- " + item)
