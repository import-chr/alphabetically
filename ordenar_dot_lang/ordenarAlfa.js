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

//array devuelto con la variable hazArr
const arrPalabras = hazArr(pPrueba);
//console.log(hazArr(pPrueba));

let letra, letraAlfa, pabsLetra = 0;

//verifica cada palabra en arrPalabras
arrPalabras.forEach(pab => {
  if(pab[letra] == alfa[letraAlfa]) {
    //aumentar la letra
    //mientras tenga letras va a seguir aumentando letra
  }
});
