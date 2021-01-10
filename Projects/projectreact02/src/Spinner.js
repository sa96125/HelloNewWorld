import React from 'react';

const Spinner = props => {
  return (
    <div className="ui active inverted dimmer">
      <div className="ui text loader">{props.message}</div>
    </div>
  );
};

// 깔끔하게 디폴트값 지정하기.
Spinner.defaultProps = {
  message: 'Loading..'
}

export default Spinner;