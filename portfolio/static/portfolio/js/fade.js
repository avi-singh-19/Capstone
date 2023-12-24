var opacity = 0;
var intervalId = 0;

function fadeIn(){
    intervalId = setInterval(show,25);
}

function show(){
    var elements = document.querySelectorAll('.fade-in');

    elements.forEach(function(element) {
        if (opacity < 1) {
            opacity += 0.01;
            element.style.opacity = opacity;
        } else {
            clearInterval(intervalId);
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    fadeIn();
});