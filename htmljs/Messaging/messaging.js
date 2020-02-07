var textArea = document.getElementById("messageList");
var textBox = document.getElementById("textbox")
function sendMessage(message) {
  console.log(message) //debugging
  if (message == ""){
    return //stops flooding page with empty paragraphs
  }
  else {
    var element = document.createElement("p");
    var t = document.createTextNode(message);
    element.appendChild(t);
    textArea.appendChild(element)
    textbox.value = ""; //clear textbox so user doesn't have to do it manually.
    var time = new Date().toLocaleTimeString();
    var telement = document.createElement("p");
    telement.id = "timeText";
    var tt = document.createTextNode(time);
    telement.appendChild(tt);
    element.appendChild(telement);
    element.scrollIntoView(false);
  }
}
