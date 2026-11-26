#!/usr/bin/env python3

import string
import random

def numalt():
    l = list(string.ascii_lowercase)
    print(l)
    random.shuffle(l)
    print(l)
    result = ''.join(l)

    return result


res = numalt()
print(res)