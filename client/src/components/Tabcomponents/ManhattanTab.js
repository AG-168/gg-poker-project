import React from "react";
import Skateparkcard from "./SkateparkCard";

function ManhattanTab ({manhattanParks}) {

    const cardDisplay = manhattanParks.map((park)=>{
        return <Skateparkcard key={park.id} id={park.id} name={park.name} address={park.address} borough={park.borough} hours={park.hours}/>
    })

  return (
    <div className="ManhattanTab">
      {cardDisplay}
    </div>
  );
};

export default ManhattanTab;