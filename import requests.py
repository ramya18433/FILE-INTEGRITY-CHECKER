import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Payloads for testing
xss_payload = "<script>alert('XSS')</script>"
sqli_payload = "' OR '1'='1"

def get_forms(url):
    """Extract all forms from a web page."""
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup.find_all("form")

def form_details(form):
    """Extract useful info from form."""
    details = {
        "action": form.attrs.get("action"),
        "method": form.attrs.get("method", "get").lower(),
        "inputs": []
    }
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        details["inputs"].append({"type": input_type, "name": input_name})
    return details

def test_xss(url):
    print(f"\n[+] Testing for XSS: {url}")
    forms = get_forms(url)
    for form in forms:
        details = form_details(form)
        data = {}
        for input_field in details["inputs"]:
            if input_field["name"]:
                data[input_field["name"]] = xss_payload
        target_url = urljoin(url, details["action"])
        if details["method"] == "post":
            res = requests.post(target_url, data=data)
        else:
            res = requests.get(target_url, params=data)
        if xss_payload in res.text:
            print(f"❗ Possible XSS vulnerability found in form at: {target_url}")
        else:
            print(f"✔ No XSS vulnerability in form at: {target_url}")

def test_sqli(url):
    print(f"\n[+] Testing for SQL Injection: {url}")
    parsed = urlparse(url)
    if parsed.query:
        base = url.split('?')[0]
        params = parsed.query.split('&')
        for param in params:
            key = param.split('=')[0]
            test_url = f"{base}?{key}={sqli_payload}"
            res = requests.get(test_url)
            errors = ["sql syntax", "mysql", "native client", "ORA-"]
            for error in errors:
                if error.lower() in res.text.lower():
                    print(f"❗ Possible SQL Injection at: {test_url}")
                    break
            else:
                print(f"✔ No SQL Injection detected in: {test_url}")
    else:
        print("⚠ No query parameters found to test SQLi.")

def main():
    print("Web Application Vulnerability Scanner")
    target = input("Enter the URL to scan (with http/https): ").strip()

    test_sqli(target)
    test_xss(target)

if _name_ == "_main_":
    main()