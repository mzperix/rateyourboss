import React, { Component } from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    bosses: []
  }

  componentDidMount() {
    axios.get(`http://demo3062747.mockable.io/search/?query=name`)
      .then(res => {
        const bosses = res.data;
        this.setState({bosses});
      })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <p>
            Searches from API:
          </p>
          <p>
            {this.state.bosses.map((boss) => boss.name)}
            // other attributes include boss.phot_url and boss.profile_url
          </p>
        </header>
      </div>
    );
  }
}

export default App;
