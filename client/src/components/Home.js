import React from "react";
import { NavLink } from "react-router-dom";

function Home () {
  return (
    <div>
      <h1>Welcome to Park & Skate</h1>
      <p>Park & skate is a website where you can find all the skateparks in New York City and Los Angeles. 
        Sign up and leave a review for your fellow skaters.
      </p>
      <nav>
        
        <div>
        <NavLink    to="/skateparks"    className="nav-link">Skateparks</NavLink>
        </div>
        <div>
        <NavLink    to="/login"    className="nav-link">Login</NavLink>
        </div>
        <div>
        <NavLink    to="/signup"    className="nav-link">Signup</NavLink>
        </div>
    </nav>
    </div>
  );
}

export default Home;