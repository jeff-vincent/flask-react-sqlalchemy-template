import React, {Component} from 'react';

class Controls extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
        count: 1,
    }
  }

  printCount(e) {
      console.log(this.state.count);
  }

  render() {
    return (
      <div >
        <button onClick={this.printCount.bind(this)}>Counter</button>
      </div>
    )
  }
}

export default Controls;