import React from "react";

function Skateparks () {
    
    function handleClick() {
        window.location.assign("/");
    }
    
    return (
        <div>
        <h1>Skateparks</h1>
        <p>Skateparks Page</p>
        
        <button onClick={handleClick}>Back to Home Page</button>
        </div>
    );
}

export default Skateparks;