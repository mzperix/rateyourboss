import React from 'react';
import { render } from 'react-dom'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import './index.css';
import App from './App';
import Boss from './Boss';
import * as serviceWorker from './serviceWorker';

render((
    <Router>
        <div>
        <Route exact path="/" component={App} />
        <Route path="/profile" component={Boss} />
        </div>
    </Router>
  ), document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
