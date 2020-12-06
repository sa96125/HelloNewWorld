
var canvas = document.querySelector("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var pen = canvas.getContext('2d');

var mouse = {
    x: undefined,
    y: undefined
}

var colorAraay = [
    'pink',
    'red',
    'skyblue',
    'black',
    'green'
]

var maxradius = 40;
var minradius = 2;

window.addEventListener('resize', function (event) {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init();
})

window.addEventListener('mousemove', function (event) {
    mouse.x = event.x;
    mouse.y = event.y;
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
        if (this.y + this.radius > innerHeight || this.y - this.radius < 0) {
            this.dy = -this.dy;
        }
        this.x += this.dx;
        this.y += this.dy;

        if (mouse.x - this.x < 50 && mouse.x - this.x > -50 && mouse.y - this.y < 50 && mouse.y - this.y > -50) {
            if (this.radius < maxradius) {
                this.radius += 1;
            }
        } else if (this.radius > this.minradius) {
            this.radius -= 1;
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

    for (var i = 0; i < 100; i++) {
        var x = Math.random() * (innerWidth - (radius * 2)) + radius;
        var y = Math.random() * (innerHeight - (radius * 2)) + radius;
        var dx = (Math.random() - 0.5) * 5;
        var dy = (Math.random() - 0.5) * 5;
        var radius = Math.random() * 10 + 10;
        circleArray.push(new Circle(x, y, dx, dy, radius));
    }

}


var circleArray = [];
init();
animate();