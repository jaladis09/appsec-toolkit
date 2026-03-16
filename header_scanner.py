import requests
import sys

SECURITY_HEADERS = {
    "Strict-Transport-Security": "Enforces HTTPS",
    "X-Frame-Options": "Prevents clickjacking",
    "X-Content-Type-Options": "Stops MIME sniffing",
    "Content-Security-Policy": "Controls resource loading",
    "Referrer-Policy": "Controls referrer info",
    "Permissions-Policy": "Restricts browser features",
}

def check_headers(url):
    print(f"\nScanning: {url}\n")
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        for header, description in SECURITY_HEADERS.items():
            if header in headers:
                print(f"  [PASS]  {header}")
            else:
                print(f"  [MISS]  {header} — {description}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 header_scanner.py https://example.com")
    else:
        check_headers(sys.argv[1])
