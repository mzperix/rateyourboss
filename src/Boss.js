import React, { Component } from 'react';
import axios from 'axios'
import logo from './logo.svg';

class Boss extends Component {
  state = {
    boss: {}
  }

  componentDidMount() {
    axios.get(`http://demo3062747.mockable.io/profile/123`)
      .then(res => {
        const boss = res.data;
        this.setState({boss});
      })
  }

  render() {
    return (
      <div>
          <p>
            Searches from API:
          </p>
          <p>
            {this.state.boss.name}
          </p>
      </div>
    );
  }
}

export default Boss;
