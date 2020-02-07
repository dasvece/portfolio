document.getElementById('calculate').onclick = function(){
  var a = parseFloat(document.getElementById('number1').value);
  var b = parseFloat(document.getElementById('number2').value);
  alert("Answer: " + avg(a,b));
}

function avg(a, b){
  console.log("clicked")
  console.log(a)
  console.log(b)
  return((a + b)/2);
}
