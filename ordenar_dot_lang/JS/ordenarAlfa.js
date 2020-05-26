const alfa = [
  "a", "b", "c", "d", "e",
  "f", "g", "h", "i", "j",
  "k", "l", "m", "n", "ñ",
  "o", "p", "q", "r", "s",
  "t", "u", "v", "w", "x", "y", "z"
];

//puede editar este string
const pPrueba = "hola ordename de manera alfebatica teniendo varias coincidencias alteradas para probar el algoritmo";

const hazArr = (palabras) => {
  let arrCreado = palabras.split(" ");

  return arrCreado;
};

const borraItem = (arR, item) => {
  let i = arR.indexOf(item);

  i !== -1 && arR.splice(i, 1);
};

//array devuelto con la variable hazArr
const arrPalabras = hazArr(pPrueba);
//console.log(arrPalabras);

let letra = 0, letraAlfa = 0, pabsLetra = 0;

let pabsRe = [];

//verifica letra y añade palabra a pabsRe
function verif(arr) {
  for(let i = 0; i < arr.length; i++) {
    const pabs = arr[i]

    if(pabs[letra] == alfa[letraAlfa]) {
      pabsRe.push(pabs);
      borraItem(arr, pabs);
      i--;
    }
  }

  if(!arr.includes([][letra] == alfa[letraAlfa])) {
    letraAlfa++;
  }

  while(arr.length > 0) {
    verif(arr);
  }
  
  return pabsRe;
}

const verifArr = verif(arrPalabras);
console.log(letraAlfa);
console.log(verifArr);
console.log(arrPalabras);
