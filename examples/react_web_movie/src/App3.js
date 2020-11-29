import React from "react";
import axios from "axios";
import Movies from "./App4"

class App3 extends React.Component {
    // 사용할 데이터들을  욧다가 넣는 구만~
    state = {
        isLoading: true,
        movies: []
    };

    //자바스크립트한테 이거 다운받을 때까지 기다려줘 왜냐면 이거 오래걸리니까.
    //헤이 너 이거 언제 실행될지 모르겠는데 (비동기식)이 함수 실행 할 때 기다려야할 순간이 올거야. 괜찮??
    //ㅇㅋ 근데 뭘? awit 이하를 실행할 때 잠깐 기다려줘
    getMovies = async () => {
        // movies.data.movies  객체로 받으니까 그안의 프롭 안에 프롭안에 값을 es6에서 이렇게 표현.
        const { data: { data: { movies } } } = await axios.get("https://yts-proxy.nomadcoders1.now.sh/list_movies.json");
        this.setState({ movies, isLoading: false });
    };

    componentDidMount() {
        // setTimeout(() => {
        //     this.setState({ isLoading: false });
        // }, 6000);
        this.getMovies();

    };

    render() {
        const { isLoading, movies } = this.state;
        return <div> {isLoading ? "Loading ... " : movies.map(movie => {
            return <Movies key={movie.id} id={movie.id} year={movie.year} title={movie.title} summary={movie.summary} />
        })} </div>;

    }
}

export default App3;
