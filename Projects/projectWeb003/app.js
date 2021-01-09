const btnOpen = document.getElementById('open');
const btnClose = document.getElementById('close');
const container = document.querySelector('.circle_container')
const content = document.querySelector('.content')

btnOpen.addEventListener('click', () => {
    container.classList.add('show_navi1');
    content.classList.add('show_navi2');
})

btnClose.addEventListener('click', () => {
    container.classList.remove('show_navi1');
    content.classList.remove('show_navi2');
})