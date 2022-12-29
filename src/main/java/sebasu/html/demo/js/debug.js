//when debug is true, show a border around each dic element
//and show the element id and class on the top left corner
let debug = false;

function debugElement(element) {
    if (debug) {
        element.style.border = "1px solid red";
        let id = element.getAttribute("id");
        let className = element.getAttribute("class");
        let text = "";
        if (id) {
            text += id;
        }
        if (className) {
            text += " " + className;
        }
        if (text) {
            let div = document.createElement("div");
            div.style.position = "absolute";
            div.style.top = "0px";
            div.style.left = "0px";
            div.style.backgroundColor = "white";
            div.style.color = "red";
            div.style.padding = "2px";
            div.style.fontSize = "10px";
            div.style.fontFamily = "sans-serif";
            div.innerHTML = text;
            element.appendChild(div);
        }
    }
}

//call debugElement on each element on document ready if debug is true
$(document).ready(function() {
    if (debug) {
        let elements = document.getElementsByTagName("*");
        for (let i = 0; i < elements.length; i++) {
            debugElement(elements[i]);
        }
    }
});