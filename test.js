// program to generate random strings

// declare all characters
const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ';


  //let letter = generateString(4);
  //document.getElementById("p1").innerHTML = letter;
  document.getElementById("submitBtn").addEventListener("click", () => {
    let letter = generateString(4);
    document.getElementById("submitBtn").innerHTML = letter;
  });


function generateString(length) {
    let result = ' ';
    const charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }

    alert(result);
    return result;
}


