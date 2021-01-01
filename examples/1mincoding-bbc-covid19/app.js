(() => {
    const stepElems = document.querySelectorAll('.step');
    const graphElems = document.querySelectorAll('.graphic-item');

   
    for (let i = 0; i < stepElems.length; i++) {
        stepElems[i].dataset.index = i;
        graphElems[i].dataset.index = i;
    }

    var currentVisible =graphElems[0].classList.add('visible');
    
    window.addEventListener('scroll', () => {
        let step;
        let boundingRect;

        for (let i = 0; i < stepElems.length; i++) {
            step = stepElems[i];
            boundingRect = step.getBoundingClientRect();
            

            if (boundingRect.top > window.innerHeight * 0.1 && boundingRect.top < window.innerHeight * 0.8) {
                if (currentVisible) {
                    currentVisible.classList.remove('visible')
                }        
                currentVisible=graphElems[i];
                currentVisible.classList.add('visible');
            }
        }
    })

})();