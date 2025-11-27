# url_feature_extractor.py

import re
import pandas as pd

def extract_numeric_features(url):
    return {
        "url_length": len(url),
        "num_dots": url.count('.'),
        "has_ip": int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        "num_hyphens": url.count('-'),
        "num_slashes": url.count('/'),
        "has_https": int(url.lower().startswith("https")),
        "has_at": int('@' in url),
        "num_digits": sum(c.isdigit() for c in url),
        "num_params": url.count('?') + url.count('&') + url.count('=')
    }

def get_feature_dataframe(urls):
    # urls = list of strings
    return pd.DataFrame([extract_numeric_features(url) for url in urls])
