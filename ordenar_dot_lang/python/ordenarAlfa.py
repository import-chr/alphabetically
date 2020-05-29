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
#print(arrPalabras)

#cambia el index de los elementos
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
	# variables para iterar en arr y en sus index
	letra_alfa = 0
	pos_letra = 0
	pabs = 0
	len_arr = len(arr)
	# print(len_arr)


	# cambia las palabras de arr si empiezan con letra_alfa
	for palabra in arr:
		llama_obtener_index = obtener_index(arr, palabra)
		llama_comp_arrays = comp_arrays(arr_const, arr_palabras)

		if palabra[pos_letra] == alfab[letra_alfa]:
			cambiaIndex(arr, llama_obtener_index, llama_comp_arrays)
			# print("ok")
		else:
			pass
            # print("no")

		# letra_alfa no aumentó
		if letra_alfa == 0:
			print("letra_alfa no aumentó aquí, por lo que no busca la siguiente letra")

	# aumenta letra_alfa si ya cambió todas las palabras que inician con letra_alfa
	for i in range(len_arr):
		if arr[pabs][0] == alfab[letra_alfa]:
			pabs += 1
			# print(pabs)
		else:
			letra_alfa += 1
			# print(variable_aumentar)

	# auxiliar, me dice si letra_alfa aumenta correctamente
	if letra_alfa == 0:
		print("el valor de letra_alfa es: " + str(letra_alfa) + " pero, no va a buscar demás letras")
	else:
		print("el valor de letra_alfa es: " + str(letra_alfa) + ", va a buscar demás letras")

	return " ".join(arr)

p1 = ordena(arr_palabras)
print(p1)
