# Práctica de Cifrado Monoalfabético y Criptoanálisis (`cryptoan`)

Trabajo en **Python 3** centrado en el cifrado monoalfabético (con clave en la primera línea del fichero cifrado) y en el criptoanálisis por análisis de frecuencias utilizando *El Quijote* (`ElQuijote.txt`) y *Hamlet* (`Hamlet.txt`) como textos de referencia.

## Qué se ha desarrollado y trabajado

- **Función `metrics(ficheroIn, skip_first=False)`:** lee el contenido en minúsculas, cuenta las apariciones de cada letra de `string.ascii_lowercase`, ordena el resultado de mayor a menor frecuencia y permite omitir la primera línea (`next(entry, None)`) al analizar ficheros cifrados que guardan la clave en la línea inicial.
- **Extracción del top `N`:** obtención de las `N` letras más frecuentes (convertidas a entero desde `sys.argv[4]`) tanto para las referencias en español e inglés como para el fichero cifrado.
- **Lectura de ficheros y control de líneas:** uso de `read()`, `split("\n")`, `lines[1:]` y `next(entry, None)` para trabajar con el texto sin incluir la clave de la primera línea.
- **Bucle de sustitución parcial y escritura de salida:** recorrido carácter a carácter sobre el texto cifrado (saltando la primera línea), comparando hasta `min(n, len(nSp), len(nEn))`, usando `c.isalpha()` y una bandera `sustituida` con `break` para escribir cada carácter una sola vez y conservar espacios, saltos de línea, puntuación y letras fuera del top `N`.

## Ejecución

```bash
./cryptoan.py ficheroEntrada -o ficheroSalida N

# Práctica de Cifrado Monoalfabético y Criptoanálisis (`cryptoan`)

Trabajo en **Python 3** centrado en el cifrado monoalfabético (con clave en la primera línea del fichero cifrado) y en el criptoanálisis por análisis de frecuencias utilizando *El Quijote* (`ElQuijote.txt`) y *Hamlet* (`Hamlet.txt`) como textos de referencia.

## Qué se ha desarrollado y trabajado

- **Función `metrics(ficheroIn, skip_first=False)`:** lee el contenido en minúsculas, cuenta las apariciones de cada letra de `string.ascii_lowercase`, ordena el resultado de mayor a menor frecuencia y permite omitir la primera línea (`next(entry, None)`) al analizar ficheros cifrados que guardan la clave en la línea inicial.
- **Extracción del top `N`:** obtención de las `N` letras más frecuentes (convertidas a entero desde `sys.argv[4]`) tanto para las referencias en español e inglés como para el fichero cifrado.
- **Lectura de ficheros y control de líneas:** uso de `read()`, `split("\n")`, `lines[1:]` y `next(entry, None)` para trabajar con el texto sin incluir la clave de la primera línea.
- **Bucle de sustitución parcial y escritura de salida:** recorrido carácter a carácter sobre el texto cifrado (saltando la primera línea), comparando hasta `min(n, len(nSp), len(nEn))`, usando `c.isalpha()` y una bandera `sustituida` con `break` para escribir cada carácter una sola vez y conservar espacios, saltos de línea, puntuación y letras fuera del top `N`.

## Ejecución

```bash
./cryptoan.py ficheroEntrada -o ficheroSalida N
