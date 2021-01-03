import { Polygon } from './polygon.js';

class App {
    // 1. 객체는 캔버스도구를 가져오고
    // 2. 캔버스 화면의 크기를 어떻게 할 것인지
    // 3. 무엇을 계속 그려낼지 정함.
    constructor() {

        // 캔버스 도구 셋팅
        this.canvas = document.createElement('canvas'); // 자바스크립트로 엘리먼트 canvas 생성:)
        document.body.appendChild(this.canvas);  // 문서에 추가.
        this.ctx = this.canvas.getContext('2d'); // 캔버스 그리기 도구:)

        // 캔버스 화면 셋팅
        this.pixelRatio = window.devicePixelRatio > 1 ? 2 : 1; // 머임?  추측 > 맥프로를 위한 조치일듯?
        window.addEventListener('resize', this.resize.bind(this), false); // 브라우저 창이 조정될때마다 reize 재조정하기 위함.
        this.resize();

        // 변경되는 그림
        window.requestAnimationFrame(this.animate.bind(this)); // 계속 그려야할 것들 호출.
    }

    resize() {
        // 윈도우 실제 크기 가져옴
        this.stageWidth = document.body.clientWidth;
        this.stageHeight = document.body.clientHeight;

        // 리사이즈 될때마다 변경되니까 캔버스 너비랑, 높이 계속 업데이트 
        this.canvas.width = this.stageWidth * this.pixelRatio;
        this.canvas.height = this.stageHeight * this.pixelRatio;
        this.ctx.scale(this.pixelRatio, this.pixelRatio);

        // 삼격형 위치 정하기
        this.polygon = new Polygon(
            this.stageWidth / 2,
            this.stageHeight / 2,
            this.stageHeight / 4,
            3
        );
    }

    animate() {
        window.requestAnimationFrame(this.animate.bind(this));
        this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight); // 기존에 있는 그림 지우고
        this.polygon.animate(this.ctx); // 수정된 값으로 다시 그림
    }
}

// 페이지 로드되면 자동으로 app객체 생성
window.onload = () => {
    new App();
}