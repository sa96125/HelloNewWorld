class App {
    constructor() {
        this.canvas = document.createElement('canvas'); // 자바스크립트로 엘리먼트 canvas 생성:)
        document.body.appendChild(this.canvas);  // 문서에 추가.
        this.ctx = this.canvas.getContext('2d'); // 캔버스 그리기 도구:)

        this.pixelRatio = window.devicePixelRatio > 1 ? 2: 1; // 머임?  추측 > 맥프로를 위한 조치일듯?
        
        window.addEventListener('resize', this.resize.bind(this), false); // 브라우저 창이 조정될때마다 reize 재조정하기 위함.
        window.requestAnimationFrame(this.animate.bind(this)); // 애니메이션을 반복적으로 그려주기위한 호출.
    }

    // 윈도우가 재조정 될때마다 크기를 재 업로드 해야함.
    resize() {
        this.stageWidth = document.body.clientWidth;
        this.stageHeight = document.body.clientHeight;

        this.canvas.width = this.stageWidth * this.pixelRatio;
        this.canvas.height = this.stageHeight * this.pixelRatio;
        this.ctx.scale(this.pixelRatio, this.pixelRatio);
    }
    
    // 그리기 함수
    animate(){
        window.requestAnimationFrame(this.animate.bind(this)); //화면에 animation 호출
        this.ctx.clearRect(0,0, this.stageWidth, this.stageHeight); // 화면에 있는 것 삭제
    }
}
window.onload= () => {
     new App;
}