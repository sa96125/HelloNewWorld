const PI2 = Math.PI * 2; // 360도

// 화면에 그려진 삼각형의 객체
export class Polygon {

    // x,y좌표, 반지름, 면의 갯수
    constructor(x, y, radius, sides) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.sides = sides;
        this.rotate = 0;
    }

    // 삼각형 그리기
    animate(ctx) {
        ctx.save();
        ctx.fillStyle = '#000'; // 채울 색갈
        ctx.beginPath(); // 그림 시작

        const angle = PI2 / this.sides;

        ctx.translate(this.x, this.y);

        for (let i = 0; i < this.sides; i++) {
            const x = this.radius * Math.cos(angle * i);
            const y = this.radius * Math.sin(angle * i);

            (i == 0) ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
        }

        ctx.fill(); // 지정한 색으로 채우기
        ctx.closePath(); // 그림 끝
        ctx.restore();
    }

}