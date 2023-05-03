import React , {useEffect, useState} from 'react';
import {Routes, Route} from 'react-router-dom';
import '../App.css';

import Home from './Home';
import Navbar from './Navbar';
import Skateparks from './Skateparks';
import Signup from './Signup';
import Login from './Login';
import Logout from './Logout';



function App() {
  const [user, setUser] = useState(null);
  const [skateparks, setSkateparks] = useState([]);
  
  useEffect(() => {
    fetch('/api/skateparks')
      .then(res => res.json())
      .then(data => {
        setSkateparks(data);
        console.log(data)
      })
  }, [])




  return (
    <div className="App">
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/skateparks" element={<Skateparks skateparksdata={skateparks}/>}  />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="*" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;