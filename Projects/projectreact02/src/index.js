import React from 'react';
import ReactDOM from 'react-dom';
import SeasonDisplay from './SeasonDisplay';
import Spinner from './Spinner';

class App extends React.Component {
    // 스테이트 영역 설정 즉, 생성자영역에서 한번 값들이 할당 되는 객체
    // 이 부분이 변할 때는 리랜더 발생.
    state = {
        lat: null,
        errorMessage: ''
    };

    // cdm함수는 초기값이 렌더된 이후 즉시 실행되는 함수
    // 리액트는 이곳에 data-load를 위한 함수를 넣을 것을 권고한다.
    // load가 끝나면 콜백함수 실행
    componentDidMount() {
        window.navigator.geolocation.getCurrentPosition(
            position => this.setState({ lat: position.coords.latitude }),
            err => this.setState({ errorMessage: err.message })
        )
        // 이 함수가 변경한 값을 cdu함수가 바로 캐치해서 rerendering를 진행한다.
    }

    // helper
    renderContent() {
        if (this.state.errorMessage && !this.setState.lat) {
            return <div>Error : {this.state.errorMessage}</div>;
        }

        if (!this.state.errorMessage && this.state.lat) {
            return <SeasonDisplay lat={this.state.lat} />;
        }

        return <Spinner message="Please accept location request!" />;
    }
    // only set JSX
    // 반드시 기본 리턴값을 가져야 한다.
    render() {
        return this.renderContent();
    }
}

// 컴포넌트 내용을 virtual dom에서 수정
ReactDOM.render(<App />, document.querySelector('#root'));
