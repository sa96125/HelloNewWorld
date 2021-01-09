// 리액트 필요한 라이브러리 npm모듈에서 가져오기
import React from 'react';
import ReactDOM from 'react-dom';
import CommentDetail from './CommentDetail';
import faker from 'faker';

// 컴포넌트(jsx)생성
const App = () => {
    return (
        <div className="ui container comments">
            <CommentDetail
                avatar={faker.image.cats()}
                author={faker.name.firstName()}
                timeAgo={faker.time.recent()}
                content={faker.lorem.sentence()}
            />
            <CommentDetail
                avatar={faker.image.people()}
                author={faker.name.firstName()}
                timeAgo={faker.time.recent()}
                content={faker.lorem.sentence()}
            />
            <CommentDetail
                avatar={faker.image.animals()}
                author={faker.name.firstName()}
                timeAgo={faker.time.recent()}
                content={faker.lorem.sentence()}
            />
        </div>
    );
};

// 컴포넌트 HTML에 보이기.
ReactDOM.render(<App />, document.querySelector('#root'));

