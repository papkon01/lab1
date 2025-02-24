import requests  

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input("Enter URL:\t ")
  
if not url.startswith('https://'):
    url = 'https://' + url 
    
print(url)


with requests.get(url) as response:  # το αντικείμενο response
    print("\nRESPONSE HEADER")
    for key, value in response.headers.items():
        print(f"{key:30s} {value}")

server_info = response.headers.get("Server", "Unknown")
print(f"\nServer Information: {server_info}")

cookies = response.cookies
if cookies:
    print("\n=== Cookies Set by the Server ===")
    for cookie in cookies:
        print(f"{cookie.name}: {cookie.value}")
else:
    print("\nNo cookies were set by the server.")