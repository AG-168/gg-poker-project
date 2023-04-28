import React from 'react';
import {Routes, Route} from 'react-router-dom';
import '../App.css';

import Home from './Home';
import Member from './Member';
import Skateparks from './Skateparks';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/member" element={<Member />} />
        <Route path="/skateparks" element={<Skateparks />} />
      </Routes>
    </div>
  );
}

export default App;