import "../App.css"
import React from "react";
import {NavLink} from "react-router-dom"

function NavBar () {


    return (
        <nav id="navBar">
            <NavLink    to="/"    className="nav-link">Home</NavLink>
            <NavLink    to="/skateparks"    className="nav-link">Skateparks</NavLink>
            <NavLink    to="/signup"    className="nav-link">Signup</NavLink>
            <NavLink    to="/login"    className="nav-link">Login</NavLink>
            <NavLink    to="/logout"    className="nav-link">Logout</NavLink>
        </nav>
    )
}

export default NavBar