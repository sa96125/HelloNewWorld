import { Polygon } from './polygon.js';

class App {
    constructor() {
        this.canvas = document.createElement('canvas'); // 자바스크립트로 엘리먼트 canvas 생성:)
        document.body.appendChild(this.canvas);  // 문서에 추가.
        this.ctx = this.canvas.getContext('2d'); // 캔버스 그리기 도구:)

        this.pixelRatio = window.devicePixelRatio > 1 ? 2 : 1; // 머임?  추측 > 맥프로를 위한 조치일듯?

        this.resize();
        window.addEventListener('resize', this.resize.bind(this), false); // 브라우저 창이 조정될때마다 reize 재조정하기 위함.
        window.requestAnimationFrame(this.animate.bind(this));
    }

    resize() {
        this.stageWidth = document.body.clientWidth;
        this.stageHeight = document.body.clientHeight;

        this.canvas.width = this.stageWidth * this.pixelRatio;
        this.canvas.height = this.stageHeight * this.pixelRatio;
        this.ctx.scale(this.pixelRatio, this.pixelRatio);

        this.polygon = new Polygon(
            this.stageWidth / 2,
            this.stageHeight / 2,
            this.stageHeight / 3,
            5
        );
    }

    animate() {
        window.requestAnimationFrame(this.animate.bind(this));
        this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);
        this.polygon.animate(this.ctx);
    }
}

window.onload = () => {
    new App();
}