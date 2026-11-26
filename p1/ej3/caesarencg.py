#!/usr/bin/env python3
#First we have to create the plaintext 
import sys
import string
string.ascii_lowercase
string.ascii_uppercase 

encrypt = ""
i=0

if len(sys.argv) < 5:
    print("USO: $caesar k entrada.txt -o salida.enc")
    exit(1)

fileIn = sys.argv[2]
fileOut = sys.argv[4]
k = int(sys.argv[1])



with open(fileIn, 'r') as entry:

    #limpiamos el contenido de saltos 
    content = entry.read()
    lines = content.split('\n')
    


    with open(fileOut, 'w') as out:
        
        for low in lines:
            low = low.lower()
        

            for c in low:
                if c.isalpha():
                    #ord da el numero ASCII de la letra
                    aux = ((ord(c) - ord('a')) + k) % 26
                    aux = chr(ord('a')+aux)
                    c = aux.upper()
            
                encrypt += c
                
        
            if i == len(lines)-1 :
                 out.write(encrypt)
            else:
                 out.write(encrypt+"\n")
                         
            encrypt=""
            i += 1

print("¡Encriptado con exito!")
            


        