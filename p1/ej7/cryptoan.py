#!/usr/bin/env python3

import sys
import string

if len(sys.argv) < 5:
    
    print("Uso: $cryptoan ficheroEntrada -o ficheroSalida N")
    exit(-1)


fichIn = sys.argv[1]
fichOut = sys.argv[3]
n = int(sys.argv[4])


def metrics(ficheroIn, skip_first=False):
    alphabet = string.ascii_lowercase
    lista = {cont: 0 for cont in alphabet}

    with open(ficheroIn, "r", encoding="utf-8") as entry:
        if skip_first:
            next(entry, None)  # Salta la primera línea (la clave) con el cifrado

        content = entry.read()

        for c in content.lower():
            if c in lista:
                lista[c] += 1

    ordenadas = sorted(lista.items(), key=lambda x: x[1], reverse=True)
    return ordenadas


#main

English = metrics("Hamlet.txt")
print("\n"+"INGLES")
for letra, numero in English:
        print(letra + ": " + str(numero))

nEn = [letra for letra, _  in English[:n]]

Spanish = metrics("ElQuijote.txt")
print("\n"+"ESPAÑOL")

for letra, numero in Spanish:
        print(letra + ": " + str(numero))

nSp = [letra for letra, _ in Spanish[:n]]


encode = metrics(fichIn,skip_first = True)

encode = [letra for letra, _ in encode[:n]]

i=0

with open(fichIn, "r", encoding="utf-8") as entry:
    next(entry, None)
    content = entry.read()
    limite = min(n, len(nSp), len(nEn))

    with open(fichOut, "w", encoding="utf-8") as out:
        
        for c in content.lower():
            if c.isalpha():
                sustituida = False

                for i in range(limite):
                    if encode[i] == c:
                        out.write(nEn[i])  
                        sustituida = True
                        break

                if not sustituida:
                    out.write(c)
            else:
                out.write(c)

print("Desencriptacion terminada")
         
    
    
    

         
    

        
              




