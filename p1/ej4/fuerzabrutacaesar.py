#!/usr/bin/env python3
#Test to force the decoder of Caesar encrypth
import sys

encrypt = ""

if len(sys.argv) < 2:
    print("USO: $fuerzabrutacaesar entrada.enc")
    exit(1)

fileIn = sys.argv[1]





with open(fileIn, 'r') as entry:
    
    content = entry.read();
    lines = content.split("\n")


with open(fileIn, 'a') as out:

    for low in lines:
            
        low = low.lower()

        for k in range(26):

            for c in low:

                if c.isalpha():
                    aux = ((ord(c) - ord('a')) - k ) % 26
                    c = chr(ord('a')+aux)
                
                encrypt += c

            if k == 25 :
                out.write(encrypt)
            else:
                out.write(encrypt+"\n")

            encrypt = ""

   

    
           

        
        
    
print("¡Desencriptado con exito!")