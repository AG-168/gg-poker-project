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
        <NavLink    to="/member"    className="nav-link">Signup / Login</NavLink>
        <br></br>
        <NavLink    to="/skateparks"    className="nav-link">Skateparks</NavLink>
    </nav>
    </div>
  );
}

export default Home;