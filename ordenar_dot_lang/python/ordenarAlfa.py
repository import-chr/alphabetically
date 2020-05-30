alfab = (
	"a", "b", "c", "d", "e",
	"f", "g", "h", "i", "j",
	"k", "l", "m", "n", "ñ",
	"o", "p", "q", "r", "s",
	"t", "u", "v", "w", "x", "y", "z"
)

p_ordenadas = ""

p_prueba = "hola ordename de manera alfebatica teniendo varias coincidencias alteradas para probar el algoritmo bueno"
arr_palabras = p_prueba.split()
arr_const = p_prueba.split()
#print(arrPalabras)

# cuenta la cantidad de palabras con 1 letra
def cuenta_palabras_con(array, letra_):
	contador = 0

	for i in array:
		if i[0] == letra_:
			contador += 1
	
	return contador

# cuenta cuantas palabras con todas las letras del abc
def palabras_con(lista):
	lista_p_ = []

	for letra in alfab:
		p_con_ = cuenta_palabras_con(lista, letra)
		if p_con_ != 0:
			lista_p_.append(p_con_)
		else:
			lista_p_.append(0)

	return lista_p_

n_p = palabras_con(arr_const)
print(n_p)

# cambia el index de los elementos
def cambiaIndex(arreglo, v_pos, n_pos):
	arreglo[n_pos], arreglo[v_pos] = arreglo[v_pos], arreglo[n_pos]

# cambio = cambiaIndex(arrPalabras, 4, 0)
# print(arrPalabras)

#retorna el index de un elemento
def obtener_index(arr1, pab):
	return arr1.index(pab)

# inPab = obtener_index(arrPalabras, "ordename")
# print(inPab)

#compara arrays
def comp_arrays(array0, array1):
	n_pos_palabra = 0
	v_array = 0

	# si ya cambió una palabra, la nueva posición incrementa
	for i in array0:
		if array0[v_array] != array1[v_array]:
			n_pos_palabra += 1
			v_array += 1
			# print(n_pos_palabra)

	return n_pos_palabra

#ordena el arreglo
def ordena(arr):
	letra_alfa = 0
	pos_letra = 0
	llama_palabras_con = palabras_con(arr)
	# variables para iterar en arr y en sus index

	# cambia las palabras de arr si empiezan con letra_alfa
	for palabra in arr:
		llama_comp_arrays = comp_arrays(arr_const, arr_palabras)
		llama_obtener_index = obtener_index(arr, palabra)

		if palabra[pos_letra] == alfab[letra_alfa]:
			cambiaIndex(arr, llama_obtener_index, llama_comp_arrays)
			print(alfab[letra_alfa])

			if arr[llama_palabras_con[0] - 1][0] == alfab[letra_alfa]:
				letra_alfa += 1
			
			if arr[llama_palabras_con[0] + llama_palabras_con[1] - 1][0] == alfab[letra_alfa]:
				letra_alfa += 1
			# print("ok")
		else:
			pass
			# print("no")

	return " ".join(arr)

p1 = ordena(arr_palabras)
print(p1)