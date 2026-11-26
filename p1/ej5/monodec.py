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
    print("USO: $monodec fihentrada -i fichsalida")
    exit(1)

fichentry = sys.argv[1]
fichout = sys.argv[3]
encrypt = ""
i=0


with open(fichentry, 'r') as entry:

    content = entry.read()
    lines  = content.split("\n")

    with open(fichout, 'w') as out:
        
        for low in lines:

            low = low.lower()

            if i == 0:
                key = low
                out.write(key+"\n")

            else:
                for c in low:
                    
                    if c.isalpha():

                        num = key.index(c)
                        c = chr(ord('a')+num)

                    encrypt += c


            if i == len(lines)-1:

                out.write(encrypt)

            elif i != 0:
                out.write(encrypt + "\n")

            encrypt  = ""
            i += 1

print("¡Desencriptado con key aleatoria con éxito!")