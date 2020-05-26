alfab = (
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "ñ",
    "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z"
)

pOrdenadas = ""

pPrueba = "hola ordename de manera alfebatica teniendo varias coincidencias alteradas para probar el algoritmo"
arrPalabras = pPrueba.split()

print(arrPalabras)

def ordena(arr):
    for palabra in arr:
        if palabra[0] == alfab[0]:
            print("ok")
        else:
                print("no")

ordena(arrPalabras)