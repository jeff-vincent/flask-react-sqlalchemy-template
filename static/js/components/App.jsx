import React, {Component} from 'react';
import Controls from './controls';
import Display from './display';

class App extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div >
        <Display/>
        <Controls/>
    	</div>)
  }
}

export default App;
