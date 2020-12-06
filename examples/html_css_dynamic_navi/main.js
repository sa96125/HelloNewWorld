const toggleBtn = document.querySelector('.bar_togleBtn');
const menu = document.querySelector('.bar_menu');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
})


