import React from 'react';

import Button from 'react-bootstrap/Button';

import './App.css';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h4> Auto Matcher </h4>
        <div>
          <Button className="Button"> Interviews </Button>
          <Button className="Button"> Offers </Button>
        </div>
      </header>
    </div>
  );
}

export default App;
