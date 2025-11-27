# tnc_module.py

def summarize_tnc(text):
    # Simple length-based summary for testing
    return text[:400] + "..." if len(text) > 400 else text

def extract_info(text):
    text_lower = text.lower()
    findings = []
    if "location" in text_lower:
        findings.append("📍 May collect your location.")
    if "camera" in text_lower:
        findings.append("📸 May request access to camera.")
    if "microphone" in text_lower or "mic" in text_lower:
        findings.append("🎤 May request microphone access.")
    if "share" in text_lower or "third party" in text_lower:
        findings.append("🔗 May share data with third parties.")
    return findings if findings else ["✅ No sensitive permissions found (basic check)."]
