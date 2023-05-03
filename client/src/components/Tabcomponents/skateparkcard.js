import React from "react";

function Skateparkcard ({name, address, borough, hours}) {
    return (
        <div>
        <br></br>
        <h3>{name}</h3>
        <p>{address}</p>
        <p>{hours}</p>
        
        </div>
    );
}

export default Skateparkcard;