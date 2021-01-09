const progress = document.getElementById('progress');
const circles = document.querySelectorAll('.circle');
const next = document.getElementById('next');
const prev = document.getElementById('prev');

let currentActive = 0;

next.addEventListener('click', () => {
    currentActive++;
    if (currentActive > 3) {
        currentActive = 3;
    }
    update();
})

prev.addEventListener('click', () => {
    currentActive--;
    if (currentActive < 0) {
        currentActive = 0;
    }
    update();
})

function update() {
    circles.forEach((circle, idx) => {
        if (idx <= currentActive) {
            circle.classList.add('active')
        } else {
            circle.classList.remove('active')
        }
    })

    let actives = document.querySelectorAll('.active')
    progress.style.width = ((actives.length - 1) / 3) * 99 + "%";

    if (currentActive === 0) {
        prev.disabled = true;
    } else if (currentActive === circles.length - 1) {
        next.disabled = true;
    } else {
        prev.disabled = false;
        next.disabled = false;
    }
}