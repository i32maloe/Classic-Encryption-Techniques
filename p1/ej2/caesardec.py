#!/usr/bin/env python3
import sys
k = 3
encrypt = ""
i=0

if len(sys.argv) < 4:
    print("USO: $caesar entrada.enc -o salida.txt")
    exit(1)

fileIn = sys.argv[1]
fileOut = sys.argv[3]




with open(fileIn, 'r') as entry:
    
    content = entry.read();
    lines = content.split("\n")
    

    with open(fileOut,'w') as out:
        
        for low in lines:
            low = low.lower()

            for c in low:

                if c.isalpha():
                    aux = ((ord(c) - ord('a')) - k ) % 26
                    c = chr(ord('a')+aux)
            
                encrypt += c

            if i == len(lines)-1 :
                out.write(encrypt)
            else:
                out.write(encrypt+"\n")
            
            encrypt=""
            i += 1
    
print("¡Desencriptado con exito!")