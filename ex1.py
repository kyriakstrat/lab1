import requests  # εισαγωγή της βιβλιοθήκης



url = input() # προσδιορισμός του url

response = requests.get(url)
headers = response.headers
print(headers)
print()
print("The web server software is {}".format(headers['server']))
print()
try:
    a = headers['Set-Cookie'].split(';')
    for i in range(len(a)):
        if 'expires' in a[i]:
            print("cookie:{} {}".format(a[i-1],a[i]))
    print()
except:
    print('no cookies')
