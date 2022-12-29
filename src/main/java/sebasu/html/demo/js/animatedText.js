

var text = '{my}Bookmarks|dev';
var textSpans = [];
var index =0;
function createTextSpans() {

    var textSpan = document.createElement('span');
    textSpan.classList.add('text-span');
    textSpan.textContent = text[index];
    textSpans.push(textSpan);
    document.getElementById('animated-text').appendChild(textSpan);
    textSpans[index].style.opacity = 1;
    if(index>0 && index<3){
        textSpans[index].style.color = "red";
    }
    textSpans[index].style.transform = 'translateX(0)';
    if(index < text.length){ index++;
        setTimeout(createTextSpans, 100);}
}



window.addEventListener('load', function() {
    index=0;
    createTextSpans();
    }
);
