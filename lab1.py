import requests
from datetime import datetime

url = input("Enter URL:  ")
  
if not url.startswith('https://'):
    url = 'https://' + url 
    
print(url)

with requests.get(url) as response:  
    print("\n=== RESPONSE HEADER ===")
    for key, value in response.headers.items():
        print(f"{key:30s} {value}")

server_info = response.headers.get("Server", "Unknown")
print(f"\n=== Server OS ===\n {server_info}")

cookies = response.cookies
if cookies:
    print("\n=== Cookies Set by the Server ===")
    for cookie in cookies:
        if hasattr(cookie, 'expires'):
            expires_date = datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
        else:
            expires_date = "No expiration date"
        print(f"{cookie.name}: {cookie.value} (Expires: {expires_date})")
else:
    print("\nNo cookies were set by the server.")