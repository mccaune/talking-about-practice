// wait for the content of the window element
// to load, then performs the operations.
// This is considered best practice.
window.addEventListener('load', () => {

    resize(); // Resizes the canvas once the window loads
    document.querySelector(".startGame").addEventListener("click", () => {
        startPainting();
    });
    // document.querySelector(".endGame").addEventListener("click", () => {
    //     stopPainting();
    // });
    //    document.addEventListener('mousedown', startPainting);
    //    document.addEventListener('mouseup', stopPainting);
    document.addEventListener('mousemove', sketch);
    window.addEventListener('resize', resize);
    document.querySelector('.box1').style.backgroundColor = `rgb(${r()},${r()},${r()},0.5)`;
    document.querySelector('.box2').style.backgroundColor = `rgb(${r()},${r()},${r()},0.5)`;
    document.querySelector('.box3').style.backgroundColor = `rgb(${r()},${r()},${r()},0.5)`;
    document.querySelector('.box4').style.backgroundColor = `rgb(${r()},${r()},${r()},0.5)`;
    document.querySelector('.box6').style.backgroundColor = `rgb(${r()},${r()},${r()},0.5)`;
    document.querySelector('.box7').style.backgroundColor = `rgb(${r()},${r()},${r()},0.5)`;
    document.querySelector('.box8').style.backgroundColor = `rgb(${r()},${r()},${r()},0.5)`;
    document.querySelector('.box9').style.backgroundColor = `rgb(${r()},${r()},${r()},0.5)`;
    // background: linear-gradient(to left, rgba(7,27,82,1) 0%, rgba(0,128,128,1) 100%); 

});

const canvas = document.querySelector('#canvas');

// Context for the canvas for 2 dimensional operations
const ctx = canvas.getContext('2d');

// Resizes the canvas to the available size of grid element Box2
//var height1 = document.getElementsByClassName("box2")[0].clientHeight;
//var width1 = document.getElementsByClassName("box2")[0].clientWidth;
function resize() {
    ctx.canvas.width = document.getElementsByClassName("box5")[0].clientWidth;
    ctx.canvas.height = document.getElementsByClassName("box5")[0].clientHeight;

}

// Stores the initial position of the cursor
let coord = { x: 0, y: 0 };

// This is the flag that we are going to use to
// trigger drawing
let paint = false;

// Updates the coordianates of the cursor when
// an event e is triggered to the coordinates where
// the said event is triggered.
function getPosition(event) {
    coord.x = event.clientX - canvas.offsetLeft;
    coord.y = event.clientY - canvas.offsetTop;
}

// The following functions toggle the flag to start
// and stop drawing
function startPainting() {
    paint = true;
    //getPosition(event);
}

function stopPainting() {
    paint = false;
}




//<><><><><><><><><><><><><><><><><><><><><><><><>
//color changes

function r() { return Math.floor(Math.random() * 255) }

var color = `rgb(${r()},${r()},${r()}0.1);`;

// function changeColor() {
//     document.getElementById("box2").style.background = color;
// }

var height1 = document.getElementsByClassName("box5")[0].clientHeight;
//console.log(height1);
var width1 = document.getElementsByClassName("box5")[0].clientWidth;
//document.getElementById("bt").style.offsetLeft = width1;
//document.getElementById("bt").style.offsetTop = height1;

function randProc1() {
    var minimum = 20;
    var maximum = 70;
    return Math.floor(Math.random() * (maximum - minimum)) + minimum;
}

function randProc2() {
    var minimum = 35;
    var maximum = 62;
    return Math.floor(Math.random() * (maximum - minimum)) + minimum;
}

var random1 = randProc1() + '%';
var random2 = randProc2() + '%';
//console.log('bottom', random1)
//console.log('left', random2)
document.getElementById("bt").style.left = random2;
document.getElementById("bt").style.bottom = random1;


//var color = "grey"
const box1 = document.querySelector("#box1");
const box2 = document.querySelector("#box2");
const box3 = document.querySelector("#box3");
const box4 = document.querySelector("#box4");
const box6 = document.querySelector("#box6");
const box7 = document.querySelector("#box7");
const box8 = document.querySelector("#box8");
const box9 = document.querySelector("#box9");

box1.addEventListener("mouseover", function changeColor() { document.getElementById("box1").style.background = color; });
box2.addEventListener("mouseover", function changeColor() { document.getElementById("box2").style.background = color; });
box3.addEventListener("mouseover", function changeColor() { document.getElementById("box3").style.background = color; });
box4.addEventListener("mouseover", function changeColor() { document.getElementById("box4").style.background = color; });
box6.addEventListener("mouseover", function changeColor() { document.getElementById("box6").style.background = color; });
box7.addEventListener("mouseover", function changeColor() { document.getElementById("box7").style.background = color; });
box8.addEventListener("mouseover", function changeColor() { document.getElementById("box8").style.background = color; });
box9.addEventListener("mouseover", function changeColor() { document.getElementById("box9").style.background = color; });


box1.addEventListener("mouseout", event => {
    //    console.log("Mouse out");
    color = `rgb(${r()},${r()},${r()})`;
});
box2.addEventListener("mouseout", event => {
    //    console.log("Mouse out");
    color = `rgb(${r()},${r()},${r()})`;
});
box3.addEventListener("mouseout", event => {
    //    console.log("Mouse out");
    color = `rgb(${r()},${r()},${r()})`;
});
box4.addEventListener("mouseout", event => {
    //    console.log("Mouse out");
    color = `rgb(${r()},${r()},${r()})`;
});
box6.addEventListener("mouseout", event => {
    //console.log("Mouse out");
    color = `rgb(${r()},${r()},${r()})`;
});
box7.addEventListener("mouseout", event => {
    //    console.log("Mouse out");
    color = `rgb(${r()},${r()},${r()})`;
});
box8.addEventListener("mouseout", event => {
    //console.log("Mouse out");
    color = `rgb(${r()},${r()},${r()})`;
});
box9.addEventListener("mouseout", event => {
    //    console.log("Mouse out");
    color = `rgb(${r()},${r()},${r()})`;
});

const buttonFind = document.querySelector("#bt");

buttonFind.addEventListener('click', event => {
    alert('You Won!');
    window.location.reload(true);
});

function sketch(event) {
    if (!paint) return;
    ctx.beginPath();

    ctx.lineWidth = 30;

    // Sets the end of the lines drawn
    // to a round shape.
    ctx.lineCap = 'round';

    ctx.strokeStyle = color;

    // The cursor to start drawing
    // moves to this coordinate
    ctx.moveTo(coord.x, coord.y);

    // The position of the cursor
    // gets updated as we move the
    // mouse around.
    getPosition(event);

    // A line is traced from start
    // coordinate to this coordinate
    ctx.lineTo(coord.x, coord.y);

    // Draws the line.
    ctx.stroke();
}




