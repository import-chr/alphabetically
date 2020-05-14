//const words = "social-network mxn mail code maths games english chess buys tools miui nike mega anime img uvm";
//crea Array, lo ordena y lo devuelve a String
function makeN_Order_Arr(strW) {
  let arrMade = strW.split(" ").sort().join(" ");

  return arrMade;
}

//obtiene el valor del imput
function getInput() {
 return document.getElementById('inpt').value;
}

const divR = document.getElementById('divR');

//escuchamos un submit y guardamos el valor del imput en value
document.getElementById('pForm').addEventListener('submit', e => {
  e.preventDefault();

  const value = getInput();
  const ordered = makeN_Order_Arr(value);
  const par = document.createElement('p');
  const textPar = document.createTextNode(ordered);

  par.appendChild(textPar);
  document.body.insertBefore(par, divR);

  console.log(value);
  console.log(ordered);
});
