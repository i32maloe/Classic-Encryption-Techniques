#!/usr/bin/env python3

import string
import random
#Escoge una letra aleatoria del abecedario buen en este caso de la cadena ascii_lowercase
r1=random.choice(string.ascii_lowercase)
print(r1)
#Escoge dos numeros de la lista introducida
r2=random.sample([3,0,-1,4.2,55],2)
print(r2)
#Escoge un numero aleatorio entre el 1 y el 10 incluidos
r3=random.randint(1,10)
print(r3)

