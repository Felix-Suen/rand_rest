import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {

  constructor(props) {
    super(props);
    this.genRand = this.genRand.bind(this);
  }

  genRand() {
     const url = 'http://localhost:8000/rest'
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div>
          <button className='random' onClick={this.genRand}>Random Restaurant</button>
          {window.token}
        </div>
      </div>
    );
  }
}

export default App;
