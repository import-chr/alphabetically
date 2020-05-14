const alfa = ["a", "b", "c", "d", "e",
              "f", "g", "h", "i", "j",
              "k", "l", "m", "n", "ñ",
              "o", "p", "q", "r", "s",
              "t", "u", "v", "w", "x", "y", "z"];

const pPrueba = "hola ordename de manera alfebatica"; //puede editar este string

const hazArr = (palabras) => {
  let arrCreado = palabras.split(" ");

  return arrCreado;
};

const arrPalabras = hazArr(pPrueba); //array devuelto con la variable hazArr
//console.log(hazArr(pPrueba));

let letra, letraAlfa = 0;

//verificar la primera letra de la palabra
function verifLetra(pab) {
  for(let i = 0; i < arrPalabras.length; i++) {
    if(arrPalabras[i][letra] == alfa[letraAlfa]) {
      //sacar la palabra
    }
  }
}
