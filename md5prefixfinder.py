#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : md5prefixfinder.py
# Author            : tmaraval <no-mail@mail.com>
# Date              : 21.09.2018
# Last Modified Date: 21.09.2018
# Last Modified By  : tmaraval <no-mail@mail.com>

import string
import random
import hashlib
import sys

i = int(sys.argv[1])
m = hashlib.md5()
m.update("".encode('utf-8'))
ret = m.hexdigest()
while ret[0:2] != "0e":
    m = hashlib.md5()
    stringg = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(i)).encode("utf-8")
    m.update(stringg)
    ret = m.hexdigest()
    if ret[0:2] == "0e":
        print("hash found" + str(stringg))

    
