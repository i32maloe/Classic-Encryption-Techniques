#!/usr/bin/env python3
import sys

encrypt = ""

if len(sys.argv) < 5:
    print("USO: $caesar k entrada.enc -o salida.txt")
    exit(1)

fileIn = sys.argv[2]
fileOut = sys.argv[4]
k = int(sys.argv[1])
i = 0


with open(fileIn, 'r') as entry:
    
    content = entry.read();
    lines = content.split("\n")
    print(lines)

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