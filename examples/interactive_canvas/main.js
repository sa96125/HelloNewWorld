
function app() {
    var canvas = dacument.querySelector("canvas");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    var pen = canvas.getContext('2d');
    pen.fillStyle = 'rgba(0,0,0,0)';
}

