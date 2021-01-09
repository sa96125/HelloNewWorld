import React from 'react'; // 무조껀 선언해줘야하고
import ReactDOM from 'react-dom';  // 리액트 js 루트에서 렌더링 할 폴더에 선언.
import App3 from './App3';  // 같은 폴더 안에 있는 APPjs를 불러오는 선언

ReactDOM.render(    // 리액트 어플리케이션은 1개의 콤포넌트만 렌더링한다!!!
  <React.StrictMode>
    <App3 />
  </React.StrictMode>, // 콤포넌트는 HTML 를 반환하는 함수다!!! 제일중요, 콤포넌트 콤포노퉅 콘퍼논트!! JSX inly in React~
  document.getElementById('root') // root라는 이름을 가진 문서에다가 렌더링하겠다 이말임. App 콤포넌트를!!!!
);