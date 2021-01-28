const cssText = document.querySelector("h3");
const color1 = document.querySelector(".color1");
const color2 = document.querySelector(".color2");
const body = document.getElementById("background");
const randomButton = document.querySelector(".randomButton");


window.addEventListener('load', () => {
    color1.value = `#${r()}`;
    color2.value = `#${r()}`;
    setBackground();
});

function r() { return Math.floor(Math.random() * 16777215).toString(16) }

function setBackground() {
    body.style.background = `linear-gradient(to right, ${color1.value}, ${color2.value})`;
    cssText.textContent = body.style.background + ";";
}

function randomBackground() {
    randomColor1 = `#${r()}`;
    randomColor2 = `#${r()}`;
    body.style.background = `linear-gradient(to right, ${randomColor1}, ${randomColor2})`;
    cssText.textContent = body.style.background + ";";
    color1.value = randomColor1;
    color2.value = randomColor2;
}

color1.addEventListener("input", setBackground);
color2.addEventListener("input", setBackground);
randomButton.addEventListener("click", randomBackground);