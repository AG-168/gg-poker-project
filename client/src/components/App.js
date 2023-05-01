import React from 'react';
import {Routes, Route} from 'react-router-dom';
import '../App.css';

import Home from './Home';

import Skateparks from './Skateparks';
import Signup from './Signup';
import Login from './Login';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />

        <Route path="/skateparks" element={<Skateparks />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="*" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;