const alfa = [
  "a", "b", "c", "d", "e",
  "f", "g", "h", "i", "j",
  "k", "l", "m", "n", "ñ",
  "o", "p", "q", "r", "s",
  "t", "u", "v", "w", "x", "y", "z"
];

//puede editar este string
const pPrueba = "hola ordename de manera alfebatica teniendo varias coincidencias alteradas";

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
//console.log(hazArr(pPrueba));

let letra = 0, letraAlfa = 0, pabsLetra = 0;

//verifica cada letras de una palabra con el alfabeto
function verif(arr) {
  let pabsRe = [];

  arr.forEach(pabs => {
    if(pabs[letra] == alfa[letraAlfa]) {
      pabsRe.push(pabs);
      borraItem(arr, pabs);
    }
  });
  
  return pabsRe;
  //console.log(pabsRe);
}

const verifArr = verif(arrPalabras);
// console.log(verifArr);
// console.log(arrPalabras);

