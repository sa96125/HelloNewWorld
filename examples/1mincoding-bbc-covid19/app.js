(() => {
    const stepElems = document.querySelectorAll('.step');
    const graphElems = document.querySelectorAll('.graphic-item');

    //문제 해결해야 할 사항
    //첫번째 화면은 계속 보이게 해야하고
    //스크롤이벤트가 발생하면 해당사진 보이고 나머지는 삭제해야함!!
    for (let i = 0; i < stepElems.length; i++) {
        stepElems[i].dataset.index = i;
        graphElems[i].dataset.index = i;
    }

    graphElems[0].classList.add('visible');

    window.addEventListener('scroll', () => {
        let step;
        let boundingRect;

        for (let i = 0; i < stepElems.length; i++) {
            step = stepElems[i];
            boundingRect = step.getBoundingClientRect();

            if (boundingRect.top > window.innerHeight * 0.1 && boundingRect.top < window.innerHeight * 0.8) {
                graphElems[i].classList.add('visible');
            }
        }
    })

})();