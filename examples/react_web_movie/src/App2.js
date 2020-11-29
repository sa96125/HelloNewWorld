import React from "react";
import PropTypes from "prop-types";


//클래스로 만들면 리액트 콤포넌트에 많은 기능들을 사용할 수 있다
//Mount, Update, Unmount 
//리액트는 자동적으로 클래스 콤포넌트의 렌더링 함수를 실행한다!
//리액트에서는 버튼 뒤에 이벤트리스터 설정없이 바로 onClick 이용하면 쉽게 사용가능~
//state 안에 값은 밖에서 바꿀 수 없다. 왜냐면 리액트는 값이 바뀌면 무조껀 랜더하길 원하는데 임으로 바꾸면 랜더 할 수 없으니까. 
//따라서 값을 바꾸고 랜더링 할 수있게 하는 setState()함수를 사용해야한다. 
//★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★ setState()를 사용 할때마다 리액트는 자동으로 다시 또 또 매순간마다 reder을 실행 시킨다!!
class App2 extends React.Component {
    state = {
        count: 0
    };

    // 값에 접근할 때는 this.state.count  아큐먼트에 접근 할 때는 count!
    add = () => this.setState({ count: this.state.count + 1 });
    minus = () => this.setState(current => ({ count: current.count - 1 }));

    constructor() {
        console.log("첫 번째로 발생 -> 렌더링")
    }

    componentDidMount() {
        console.log("두 번째로 발생 -> 랜더링")
    }

    componentDidUpdate() {
        console.log("세 번째로 발생 -> 랜더링")
    }

    componentWillUnmount() {
        console.log("마지막으로 발생 -> 랜더링")
    }
    render() {
        return (
            <div>
                <h1>im a good boy {this.state.count}</h1>
                <button onClick={this.add}>Add</button>
                <button onClick={this.minus}>Minus</button>
            </div>
        );
    }
}

export default App2;
