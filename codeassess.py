#step 1: Registration
import json
import requests
url = "http://challenge.code2040.org/api/register"
github = "https://github.com/jbell98/code2040techassess"
token = "1b0d064d7f3fbe9bc9ab1a6ed56dc8a8"
x={'token': token, 'github': github}
total = requests.post(url, json=x)
print(total)
print(token, github)
print(total.text)
total.json()


#step 2: Reverse string
def reverse_str(text):
    url1 = 'http://challenge.code2040.org/api/reverse'
    url2 = 'http://challenge.code2040.org/api/reverse/validate'

    x["string"] = total.text[::-1]
    total = requests.post(url1, url2, json=x)
    print(total.text)
return reverse_str()
