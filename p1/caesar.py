#!/usr/bin/env python3
#First we have to create the plaintext 
import string
string.ascii_lowercase
string.ascii_uppercase 
k = 3
encrypt = ""

with open("entrada.txt", 'r') as entry:
    #limpiamos el contenido de saltos 
    content = entry.read()
    lines = content.split('\n')
    print(lines)
    with open("salida.enc", 'w') as out:
        for low in lines:
            low = low.lower()
            print(low)

            for c in low:
                if c.isalpha():
                    #ord da el numero ASCII de la letra
                    aux = ((ord(c) - ord('a')) + k) % 26
                    aux= chr(ord('a')+aux)
                    c = aux.upper()
            
                encrypt += c
                
        
            out.write(encrypt+"\n")
            encrypt = ""


            


        