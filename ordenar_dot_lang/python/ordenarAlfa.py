alfab = (
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "ñ",
    "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z"
)

p_ordenadas = ""

p_prueba = "hola ordename de manera alfebatica teniendo varias coincidencias alteradas para probar el algoritmo"
arr_palabras = p_prueba.split()
arr_const = p_prueba.split()
pos_letra = 0
letra_alfa = 0
n_pos_palabra = 0
#print(arrPalabras)

#cambia el index de los elementos
def cambiaIndex(arreglo, v_pos, n_pos):
    arreglo[n_pos], arreglo[v_pos] = arreglo[v_pos], arreglo[n_pos]

# cambio = cambiaIndex(arrPalabras, 4, 0)
# print(arrPalabras)

#retorna el index de un elemento
def obtenIndex(arr1, pab):
    return arr1.index(pab)

# inPab = obtenIndex(arrPalabras, "ordename")
# print(inPab)

#compara arrays
def comp_arrays(array0, array1, v_aumentar):
    v_array0 = 0
    v_array1 = 0

    if array0[v_array0] != array1[v_array1]:
        v_aumentar += 1

    return v_aumentar

#funcion principal, ordena el arreglo
def ordena(arr):
    for palabra in arr:
        if palabra[pos_letra] == alfab[letra_alfa]:
            cambiaIndex(arr, obtenIndex(arr, palabra), """numero""")
            # print("ok")
        else:
            pass
            # print("no")
    return arr

p1 = ordena(arr_palabras)
print(p1)
print(n_pos_palabra)