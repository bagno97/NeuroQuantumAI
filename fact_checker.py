"""
fact_checker.py
---------------
Moduł zapewniający funkcje fact-checkingu, detekcji dezinformacji i oceniania wiarygodności źródeł dla NeuroQuantumAI.
Integruje się z AIEngine, task_executor, oraz innymi modułami sieci i pamięci.
"""

import requests
from typing import List, Dict, Any
import re

# Lista zaufanych domen (możesz rozbudować)
TRUSTED_DOMAINS = [
    "gov.pl", "who.int", "wikipedia.org", "bbc.com", "reuters.com", "nature.com", "snopes.com"
]

# Przykładowe API fact-checkingowe (do rozbudowy/zastąpienia prawdziwym)
FACT_CHECK_API_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
FACT_CHECK_API_KEY = "YOUR_API_KEY"  # <-- Wstaw swój klucz API jeśli posiadasz

def is_trusted_domain(url: str) -> bool:
    """
    Sprawdza, czy adres URL należy do zaufanej domeny.
    """
    return any(domain in url for domain in TRUSTED_DOMAINS)

def fetch_from_multiple_sources(query: str) -> List[Dict[str, Any]]:
    """
    Pobiera informacje z kilku źródeł (do rozbudowy o prawdziwe API/news).
    """
    # Przykład: pobierz z Wikipedii i DuckDuckGo
    results = []
    try:
        wiki = requests.get(f"https://pl.wikipedia.org/w/api.php?action=opensearch&search={query}&limit=1&format=json", timeout=5)
        if wiki.ok:
            data = wiki.json()
            if data and len(data) > 2 and data[2]:
                results.append({
                    "source": "wikipedia.org",
                    "summary": data[2][0],
                    "url": data[3][0] if len(data[3]) > 0 else ""
                })
        ddg = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json", timeout=5)
        if ddg.ok:
            data = ddg.json()
            if data.get("AbstractText"):
                results.append({
                    "source": "duckduckgo.com",
                    "summary": data["AbstractText"],
                    "url": data.get("AbstractURL", "")
                })
    except Exception as e:
        results.append({"source": "error", "summary": str(e), "url": ""})
    return results

def check_with_fact_api(statement: str) -> Dict[str, Any]:
    """
    Sprawdza twierdzenie przez zewnętrzne API fact-checkingowe (Google Fact Check Tools).
    """
    try:
        params = {
            "query": statement,
            "key": FACT_CHECK_API_KEY
        }
        resp = requests.get(FACT_CHECK_API_URL, params=params, timeout=7)
        if resp.ok:
            data = resp.json()
            if "claims" in data and data["claims"]:
                claim = data["claims"][0]
                return {
                    "status": claim.get("text", "unknown"),
                    "claimReview": claim.get("claimReview", [])
                }
        return {"status": "unknown", "claimReview": []}
    except Exception as e:
        return {"status": "error", "details": str(e)}

def detect_fake_news_features(text: str) -> List[str]:
    """
    Wykrywa typowe cechy dezinformacji w tekście.
    """
    warnings = []
    if re.search(r"!{2,}|\?{2,}", text):
        warnings.append("Sensacyjny nagłówek lub nadmiar znaków interpunkcyjnych")
    if text.isupper():
        warnings.append("Tekst pisany wielkimi literami")
    if len(text.split()) < 8:
        warnings.append("Bardzo krótka treść — możliwy clickbait")
    if not re.search(r"https?://", text):
        warnings.append("Brak źródeł w treści")
    # Możesz dodać więcej heurystyk
    return warnings

def fact_check_pipeline(statement: str) -> Dict[str, Any]:
    """
    Główna funkcja: sprawdza twierdzenie przez kilka warstw:
    - porównuje z wieloma źródłami,
    - sprawdza przez API fact-checkingowe,
    - wykrywa cechy dezinformacji,
    - ocenia zaufanie do źródła.
    """
    results = fetch_from_multiple_sources(statement)
    fact_api = check_with_fact_api(statement)
    warnings = []
    for r in results:
        if r.get("url") and not is_trusted_domain(r["url"]):
            warnings.append(f"Źródło {r['url']} nie jest na liście zaufanych!")
    for r in results:
        warnings.extend(detect_fake_news_features(r.get("summary", "")))
    if fact_api.get("status") == "error":
        warnings.append(f"Błąd API fact-check: {fact_api.get('details')}")
    return {
        "sources": results,
        "fact_api": fact_api,
        "warnings": warnings
    }
