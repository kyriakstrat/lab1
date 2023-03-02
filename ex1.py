#name: Kyriakos Stratakos AM: 1072704

import requests  # εισαγωγή της βιβλιοθήκης


url = input() # προσδιορισμός του url

response = requests.get(url)
headers = response.headers
print(headers)
print()
#prints web Server software
print("The web server software is {}".format(headers['server']))
print()
#prints cookies if there are any
try:
    a = headers['Set-Cookie'].split(';')
    for i in range(len(a)):
        if 'expires' in a[i]:
            print("cookie:{} {}".format(a[i-1],a[i]))
    print()
except:
    print('no cookies')
