
var canvas = document.querySelector("canvas");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight - 63;
var pen = canvas.getContext('2d');

var mouse = {
    x: undefined,
    y: undefined
}

var colorAraay = [
    '#ef9a9a',
    '#ffcccb',
    '#ba6b6c',
    '#ef5350',
    '#b61827'
]

var maxradius = 40;
var minradius = 10;

window.addEventListener('resize', function (event) {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight - 63;
    init();
})

window.addEventListener('mousemove', function (event) {
    mouse.x = event.x;
    mouse.y = event.y - 63;
})

function Circle(x, y, dx, dy, radius) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;
    this.minradius = radius;

    this.color = colorAraay[Math.floor(Math.random() * colorAraay.length)];

    this.draw = function () {
        pen.beginPath();
        pen.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        // pen.strokeStyle = "orange";
        // pen.stroke();
        pen.fillStyle = this.color;
        // pen.fillStyle = colorAraay[Math.floor(Math.random() * colorAraay.length)]
        pen.fill();
    }

    this.update = function () {
        if (this.x + this.radius > innerWidth || this.x - this.radius < 0) {
            this.dx = -this.dx;
        }
        if (this.y + this.radius > canvas.height || this.y - this.radius < 0) {
            this.dy = -this.dy;
        }
        this.x += this.dx;
        this.y += this.dy;

        if (mouse.x - this.x < 20 && mouse.x - this.x > -20 && mouse.y - this.y < 20 && mouse.y - this.y > -20) {
            if (this.radius < maxradius) {
                this.radius += 1;
            }
        } else if (this.radius > this.minradius) {
            this.radius -= 1;
        } else if (mouse.x === 0 || mouse.x === canvas.width || mouse.y === 0 || mouse.y === canvas.height) {
            mouse.x = undefined;
            mouse.y = undefined;
        }
    }
}

function animate() {
    requestAnimationFrame(animate);
    pen.clearRect(0, 0, innerWidth, innerHeight);

    for (var i = 0; i < circleArray.length; i++) {
        circleArray[i].draw();
        circleArray[i].update();
    }
}

function init() {
    circleArray = [];

    for (var i = 0; i < 300; i++) {
        var x = Math.random() * (innerWidth - (radius * 2)) + radius;
        var y = Math.random() * (canvas.height - (radius * 2)) + radius;
        var dx = (Math.random() - 0.5) * 5;
        var dy = (Math.random() - 0.5) * 5;
        var radius = 20//Math.random() * 10 + 10;
        circleArray.push(new Circle(x, y, dx, dy, radius));
    }

} ß

var circleArray = [];
init();
animate();