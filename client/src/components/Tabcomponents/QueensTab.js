import React from "react";
import Skateparkcard from "./SkateparkCard";

function QueensTab ({queensParks}) {

    const cardDisplay = queensParks.map((park)=>{
        return <Skateparkcard key={park.id} name={park.name} address={park.address} borough={park.borough} hours={park.hours}/>
    })

  return (
    <div className="QueensTab">
      {cardDisplay}
    </div>
  );
};

export default QueensTab;