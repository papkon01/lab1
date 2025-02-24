import requests  # εισαγωγή της βιβλιοθήκης

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
