#!/usr/bin/env python3
import sys
import string
import random

def numalt():
    l = list(string.ascii_lowercase)
    print(l)
    random.shuffle(l)
    print(l)
    result = ''.join(l)

    return result

#main

if len(sys.argv) < 4:
    print("USO: $monoenc fihentrada -i fichsalida")
    exit(1)

fichentry = sys.argv[1]
fichout = sys.argv[3]
key = numalt()
print("Key =" + key)
encrypt = ""
i=0


with open(fichentry, 'r') as entry:

    content = entry.read()
    lines  = content.split("\n")

    with open(fichout, 'w') as out:

        out.write(key+"\n")

        for low in lines:

            low = low.lower()

            for c in low:
                
                if c.isalpha():
                    num = (ord(c)-ord('a')) % 26
                    c = key[num]

                encrypt += c


            if i == len(lines)-1:
                out.write(encrypt)
            else:
                out.write(encrypt + "\n")

            encrypt  = ""
            i += 1

print("¡Encriptado con key aleatoria con éxito!")