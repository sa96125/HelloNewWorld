import React from 'react';
import './SeasonDisplay.css';
// 각 함수의 순서도 중요함. funcktion expreetion!

// 변수객체
const seasonConfig = {
    summer: {
        text: '대프리카에 오신 것은 환영합니다.',
        iconName: 'sun'
    },
    winter: {
        text: '스바 왜케 추운거여?',
        iconName: 'snowflake'
    }
};

// 현재 날짜와 위치를 동시에 확인해서 현재의 계절을 리턴해주는 함수.
const getSeason = (lat, month) => {
    if (month > 3 && month < 10) {
        return lat > 35 ? 'summer' : 'winter';
    } else {
        return lat > 35 ? 'winter' : 'summer';
    }
}

// 화면에 시즌을 표시하는 functional component.
const SeasonDisplay = (props) => {
    const season = getSeason(props.lat, new Date().getMonth());
    // const text = season === 'winter' ? '스바 왜케 추운거여?' : '대프리카에 오신 것은 환영합니다.';
    // const icon = season === 'winter' ? 'snowflake' : 'sun';
    const { text, iconName } = seasonConfig[season];
    <i class="snowflake outline icon"></i>
    return (
        <div className={`season-display ${season}`}>
            <i className={`icon-left massive ${iconName} outline icon`} />
            <h1>{text}</h1>
            <i className={`icon-right massive ${iconName} outline icon`} />
        </div>
    );
};

export default SeasonDisplay;