//문자열
let nameString = '    my name is jake';

nameString.toUpperCase();
nameString.toLowerCase();
//양끝 s잘라버리기
nameString.trim();
nameString.indexOf('s');
//0번째 인덱스 뺀 문자열
nameString.slice(1);
nameString.replace('j', 'J');
//Math
Math.PI;
//소수 잘라버리기
Math.floor(3.099);
//반올림
Math.round(3.4);
//제곱
Math.pow(7.2);
//랜덤 1~10까지 숫자.
Math.floor(Math.random() * 9) + 1


let arrNumber = ['99', '13', '345', '4536', '33'];
let arrString = ['ellie', 'nomad', 'grid']

//기존 배열 맨 뒤에 추가
arrNumber[arrNumber.length] = '777';
console.log(arrNumber);
//기존 배열 맨 뒤에 추가
arrNumber.push('7777');
console.log(arrNumber);
//기존 배열 맨 뒤에 삭제
arrNumber.pop();
console.log(arrNumber);
//기존 배열 맨 앞에 추가
arrNumber.unshift('111');
console.log(arrNumber);
//기존 배열 맨 앞에 삭제
arrNumber.shift();
console.log(arrNumber);
//유니코드 맨 앞글자 기준으로 정렬하기
arrNumber.sort();
console.log(arrNumber);
//기존배열을 역순으로
arrNumber.reverse();
console.log(arrNumber);
//하나의 문자열로 합체( 디폴트값 ',')
arrNumber.join('');
console.log(arrNumber);
//값이 있는지 없는지 true or false
arrNumber.includes('777');
console.log(arrNumber);
//값의 인덱스를 찾고 싶을 때 (없으면 return -1)
arrNumber.indexOf('111');
console.log(arrNumber);
//범위(1~2)의 값을 복사하고 싶을 때
// let copy= arrstring.slice() 하면 기존 값을 복사한 새로운 배열 생성
arrString.slice(1, 3);
console.log(arrNumber);
//배열의 중간(인덱스)에 값을 삭제하거나 추가하고 싶을 때
//(인덱스넘버 , 삭제하고 싶은 값의 갯수 , 추가하려는 값)
arrString.splice(1, 2, '추가했당', '한개더!');
console.log(arrNumber);
