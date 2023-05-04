import "../App.css"
import React from "react";
import {NavLink, useNavigate} from "react-router-dom"

function NavBar ({updateUser}) {

    const navigate = useNavigate();

    const handleLogout = () => {
    
        fetch('/logout',{
          method:'DELETE'
        })
        .then(res => {
          if(res.ok){
              updateUser(null)
              navigate('/authentication')
          }
        })
        
       }

    return (
        <nav id="navBar">
            <NavLink    to="/"    className="nav-link">Home</NavLink>
            <NavLink    to="/skateparks"    className="nav-link">Skateparks</NavLink>
            <NavLink    to="/signup"    className="nav-link">Signup</NavLink>
            <NavLink    to="/login"    className="nav-link">Login</NavLink>
            <NavLink    to="/logout"    className="nav-link" onClick={handleLogout}>Logout</NavLink>
            <NavLink    to="/authentication"    className="nav-link">Authentication</NavLink>
        </nav>
    ) 
}

export default NavBar