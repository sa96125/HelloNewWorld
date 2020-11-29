import React from "react";
import Proptypes from "prop-types";  // 추가모듈 설치후 사용가능.

// 객체를 가지고 있는 배열. like JSON^_^
// 객체를 전달할 때 유일한 키를 전달하는 것도 중요하지만,
// 객체를 함수에 프럽(argus)을 전달할 때 정확히 전달했는지 확인 할 필요가 있다.
const singerIlike = [
  {
    id: 1,
    name: "iU",
    song: "마시멜로우",
    rating: 5
  },
  {
    id: 2,
    name: "하요시",
    song: "하울의 움직이는 성"
  },
  {
    id: 3,
    name: "j park",
    song: "sexy mommae"
  },
  {
    id: 4,
    name: "ssakthree",
    song: "ggang"
  },
];

//객체 통째로 전달하는 방법.
function Moive(props) {
  console.log(props.actor);
  return <h1>I love {props.actor}</h1>;
}

//내부 요소만 전달 ( NEW )
function Singer({ name, rating }) {
  console.log({ name });
  return (
    <div>
      <h1>I love {name}</h1>
      <h2>I rating is : {rating}</h2>
    </div>
  );
}

//얻고 싶은 프롭타임에 대한 설명을 여기다가 적어 놓는다.
Singer.prototype = {
  name: Proptypes.string.isRequired,
  rating: Proptypes.number.isRequired
};

//컴포넌트(함수)를 불러서 화면에 나타 나게 할 수 있다.
//자바스크립트처럼 사용가능 {안에다가 코드}  
//객체가 저장된 데이터타입에다가 콤포넌트의 인자로 객체 전달
//Map 함수를 이용해서 return을 콤포넌트로 해버리면 안에 각 요소 전체에 접근해서 값을 전달받고 컴포넌트의 기능을 수행한다!!
//콤포넌트로 데이터를 보낼 수도 있다. 
//map사용하여 객체를 넘겨줄때는 요소가 많아서, 요소들 전체에 대한 유니크성을 만들어 줘야하므로, 
//사용하던 안하던 객체에 고유한 Key를 콤포논트에 같이 넘겨줘야한다.
function App() {
  return (
    <div className="App">
      {singerIlike.map(person => <Singer key={person.id} name={person.name} rating={person.rating} />)}
      <Moive name="바람과 함께 사라지다" actor={["장동건", "고소영"]} />
      <Singer name="GD 2020 콘서트" actor={["IU", "GD"]} />
    </div>
  );
}

export default App;
