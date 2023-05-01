import React from "react";

function Skateparkcards ({name, address, borough, hours}) {
    return (
        <div>
        <h3>{name}</h3>
        <p>{address}</p>
        <p>{borough}</p>
        <p>{hours}</p>
        </div>
    );
}

export default Skateparkcards;