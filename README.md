# Práctica de Cifrado Monoalfabético y Criptoanálisis (`cryptoan`)

Trabajo en **Python 3** centrado en el cifrado monoalfabético (con clave en la primera línea del fichero cifrado) y en el criptoanálisis por análisis de frecuencias utilizando *El Quijote* (`ElQuijote.txt`) y *Hamlet* (`Hamlet.txt`) como textos de referencia.

## Qué se ha desarrollado y trabajado

-**Estudio y desarrollo de cifrados clásicos** como el Caesar en las primeras funciones.
.**Uso de cifrado monoalfabético y técnicas básicas de desencriptado.
- **Función `metrics(ficheroIn, skip_first=False)`:** lee el contenido en minúsculas, cuenta las apariciones de cada letra de `string.ascii_lowercase`, ordena el resultado de mayor a menor frecuencia y permite omitir la primera línea (`next(entry, None)`) al analizar ficheros cifrados que guardan la clave en la línea inicial.
- **Extracción del top `N`:** obtención de las `N` letras más frecuentes (convertidas a entero desde `sys.argv[4]`) tanto para las referencias en español e inglés como para el fichero cifrado.
- **Lectura de ficheros y control de líneas:** uso de `read()`, `split("\n")`, `lines[1:]` y `next(entry, None)` para trabajar con el texto sin incluir la clave de la primera línea.
- **Bucle de sustitución parcial y escritura de salida:** recorrido carácter a carácter sobre el texto cifrado (saltando la primera línea), comparando hasta `min(n, len(nSp), len(nEn))`, usando `c.isalpha()` y una bandera `sustituida` con `break` para escribir cada carácter una sola vez y conservar espacios, saltos de línea, puntuación y letras fuera del top `N`.

**EN
# Monoalphabetic Cipher and Cryptanalysis Assignment (`cryptoan`)

**Python 3** work focused on monoalphabetic encryption (with the key stored on the first line of the ciphertext file) and frequency-analysis cryptanalysis using *Don Quixote* (`ElQuijote.txt`) and *Hamlet* (`Hamlet.txt`) as reference texts.

## What Has Been Built and Worked On

- **Study and implementation of classical ciphers** such as Caesar in the early functions.
- **Use of monoalphabetic encryption and basic decryption techniques.**
- **`metrics(ficheroIn, skip_first=False)` function:** reads content in lowercase, counts occurrences of each letter in `string.ascii_lowercase`, sorts frequencies from highest to lowest, and supports skipping the first line (`next(entry, None)`) when analyzing ciphertext files that store the key on line one.
- **Top `N` extraction:** retrieves the `N` most frequent letters (parsed as an integer from `sys.argv[4]`) for both Spanish and English reference corpora as well as the ciphertext file.
- **File reading and line handling:** uses `read()`, `split("\n")`, `lines[1:]`, and `next(entry, None)` to process the message body without including the initial key line.
- **Partial substitution and output writing loop:** iterates character by character over the ciphertext (skipping the first line), bounds comparisons with `min(n, len(nSp), len(nEn))`, uses `c.isalpha()` and a `sustituida` flag with `break` to write each character once while preserving spaces, newlines, punctuation, and letters outside the top `N`.


## Ejecución|Usage

```bash
./cryptoan.py ficheroEntrada -o ficheroSalida N



