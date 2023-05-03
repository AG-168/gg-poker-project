import React from "react";
import Skateparkcard from "./SkateparkCard";

function BrooklynTab ({brooklynParks}) {

    const cardDisplay = brooklynParks.map((park)=>{
        return <Skateparkcard key={park.id} id={park.id} name={park.name} address={park.address} borough={park.borough} hours={park.hours}/>
    })

  return (
    <div className="BrooklynTab">
      {cardDisplay}
    </div>
  );
};

export default BrooklynTab;