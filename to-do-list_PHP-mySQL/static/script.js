var toggle = document.getElementsByClassName("check");
var i;
for (i = 0; i < toggle.length; i++) {
    toggle[i].onclick = function() {
        var change = this.parentElement.parentElement.parentElement;
        change.classList.toggle('changeColor');
    }
}
