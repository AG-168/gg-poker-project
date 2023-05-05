import React , {useEffect, useState} from 'react';
import {Routes, Route, useNavigate} from 'react-router-dom';
import '../App.css';

import Home from './Home';
import Navbar from './Navbar';
import Skateparks from './Skateparks';
import Logout from './Logout';
import Authentication from './Authentication';



function App() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  const [skateparks, setSkateparks] = useState([]);
  
  useEffect(() => {
    fetch('/api/skateparks')
      .then(res => res.json())
      .then(data => {
        setSkateparks(data);
        console.log(data)
      })
  }, [])

  

  useEffect(() => {
    fetchUser()
  },[])

  const fetchUser = () => {
    fetch('/authorized')
    .then(res => {
      if(res.ok){
        res.json().then(data => {setUser(data) 
        })
      }else {
        setUser(null)
      }
    })
}

const updateUser = (user) => setUser(user)

  



  return (
    <div className="App">
      <Navbar updateUser={updateUser}/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/skateparks" element={<Skateparks skateparksdata={skateparks}/>}  />
        <Route path="/logout" element={<Logout />} />
        <Route path="/authentication" element={<Authentication updateUser={updateUser} />} />
        <Route path="*" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;