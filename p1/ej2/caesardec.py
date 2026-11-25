#!/usr/bin/env python3
import sys
k = 3
encrypt = ""

if len(sys.argv) < 4:
    print("USO: $caesar entrada.txt -o salida.enc")
    exit(1)

fileIn = sys.argv[1]
fileOut = sys.argv[3]




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

            out.write(encrypt)
            encrypt = "\n"
        
    
print("¡Desencriptado con exito!")