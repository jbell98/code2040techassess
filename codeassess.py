import json
import requests
import datetime
from datetime import timedelta
url = "http://challenge.code2040.org/api/register"
github = "https://github.com/jbell98/code2040techassess"
token = "1b0d064d7f3fbe9bc9ab1a6ed56dc8a8"

#step 1: registration
def registration():

    x={'token': token, 'github': github}
    total = requests.post(url, json=x)
    print(total)
    print(total.text)
print(registration())

#step 2: Reverse string
url1 = 'http://challenge.code2040.org/api/reverse'
url2 = 'http://challenge.code2040.org/api/reverse/validate'


def reverse_str():
    x={'token': token}
    total = requests.post(url1, json=x)
    print(total.text)
    rev_str = total.text[::-1]
    print(rev_str)
    x={'token': token, 'string': rev_str}
    total = requests.post(url2, json=x)
    print(total.text)
print(reverse_str())

#step 3: needle in haystack
url1 = 'http://challenge.code2040.org/api/haystack'
url2 = 'http://challenge.code2040.org/api/haystack/validate'


def needleInHaystack():
    x={'token': token}
    total = requests.post(url1, json=x)
    dic = json.loads(total.text)
    needle = dic['needle']
    h = dic['haystack']
    count = 0
    for x in h:
        if x == needle:
            break
        else:
            count +=1
    i={'token': token, 'needle': count}
    total = requests.post(url2, json=i)
    print(total.text)
print(needleInHaystack())

#step 4: prefix
url1 = 'http://challenge.code2040.org/api/prefix'
url2 = 'http://challenge.code2040.org/api/prefix/validate'

def prefix():
    x={'token': token}
    total = requests.post(url1, json=x)
    dic = json.loads(total.text)
    prfx = dic['prefix']
    array = dic['array']
    empty = []
    for x in array:
        if not (x.startswith(prfx,0)):
            empty.append(x)
            
    i={'token': token, 'array': empty}
    total = requests.post(url2, json=i)
    print(total.text)
print(prefix())

#step 5: Dating Game
url1 = 'http://challenge.code2040.org/api/dating'
url2 = 'http://challenge.code2040.org/api/dating/validate'

def dateTime():
    x={'token': token}
    total = requests.post(url1, json=x)
    dic = json.loads(total.text)
    datestamp = dic['datestamp']
    interval = dic['interval']
    time = datetime.datetime.strptime(datestamp,"%Y-%m-%dT%H:%M:%SZ")
    otherTime = datetime.timedelta(seconds = interval)
    time += otherTime
    time = time.strftime('%Y-%m-%dT%H:%M:%SZ')
    i={'token': token, 'datestamp': time}
    total = requests.post(url2, json=i)
    print(total.text)
print(dateTime())
  
