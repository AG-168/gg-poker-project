import React from "react";

import Skateparkcards from "./Skateparkcards";

function Skateparks ({skateparksdata}) {

    const skateparks = skateparksdata.map((skatepark) => {
        return (<Skateparkcards key={skatepark.id} name={skatepark.name} address={skatepark.address} borough={skatepark.borough} hours={skatepark.hours} />)
    })


    
    return (
        <div>
        <h1>Skateparks</h1>

        <div>{skateparks}</div>
        
        
        </div>
    );
}

export default Skateparks;