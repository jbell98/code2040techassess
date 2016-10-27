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


#step 2: Reverse string

def Anagram(str1, str2):
    my_list = list(str2)
    num = 0
    if str1 == '' or "":
        return False
    while num <len(str1) and True:
        x = 0
        found = False
        while x < len(my_list) and not found:
            if str1(num) == my_list(x):
                found = True
            else:
                x+=1
        if found:
            my_list[x] = None
        else:
            return False

        num +=1
    return True
print(Anagram('anna', 'racecar')
