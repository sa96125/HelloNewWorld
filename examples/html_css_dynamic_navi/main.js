const toggleBtn = document.querySelector('.bar_togleBtn');
const menu = document.querySelector('.bar_menu');
const icons = document.querySelector('.bar_icons');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
})


