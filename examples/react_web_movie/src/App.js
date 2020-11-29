import React from "react";

const singerIlike = [
  {
    name:"iU",
    song:"마시멜로우"
  },
  {
    name:"하요시",
    song:"하울의 움직이는 성"
  },
  {
    name:"j park",
    song:"sexy mommae"
  },
  {
    name:"ssakthree",
    song:"ggang"
  },
];

//객체 통째로 전달하는 방법.
function Moive(props) { 
  console.log(props.actor);
  return <h1>I love {props.actor}</h1>;
}

//내부 요소만 전달 ( NEW )
function Singer({name}) { 
  console.log({name});
  return <h1>I love {name}</h1>;
}

//컴포넌트(함수)를 불러서 화면에 나타 나게 할 수 있다.
//자바스크립트처럼 사용가능 {안에다가 코드}  
//객체가 저장된 데이터타입에다가 콤포넌트의 인자로 객체 전달
//Map 함수를 이용해서 return을 콤포넌트로 해버리면 안에 각 요소 전체에 접근해서 값을 전달받고 컴포넌트의 기능을 수행한다!!
function App() {
  return (
  <div className="App">  
      {singerIlike.map(person =><Singer name={person.name} />)}    
      <Moive name="바람과 함께 사라지다" actor={["장동건","고소영"]} />                   
      <Singer name="GD 2020 콘서트" actor={["IU","GD"]} />                   
  </div>       //콤포넌트로 데이터를 보낼 수도 있다. 
  );
}

export default App;
