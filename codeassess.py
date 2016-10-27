#step 1: Registration
import json
import requests
url = "http://challenge.code2040.org/api/register"
github = "https://github.com/jbell98/code2040techassess"
token = "1b0d064d7f3fbe9bc9ab1a6ed56dc8a8"
total = requests.post(url, json={'token': token, 'github': github})
print(total)
print(token, github)
print(total.text)
total.json()
