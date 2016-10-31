import json
import requests
url = "http://challenge.code2040.org/api/register"
github = "https://github.com/jbell98/code2040techassess"
token = "1b0d064d7f3fbe9bc9ab1a6ed56dc8a8"

#step 1: registration
def registration():

    x={'token': token, 'github': github}
    total = requests.post(url, json=x)
    print(total)
    print(token, github)
    print(total.text)
print(registration())

url1 = 'http://challenge.code2040.org/api/reverse'
url2 = 'http://challenge.code2040.org/api/reverse/validate'
token = "1b0d064d7f3fbe9bc9ab1a6ed56dc8a8"

#step 2: Reverse string
def reverse_str():
    x={'token': token, 'github': github}
    total = requests.post(url1, url2, json=x)
    print (total.content)
    text = total.content
    string = text[::-1]
    print(string)
    total2 = requests.post(url2, json=x)
    print(total2.text)
print(reverse_str())



