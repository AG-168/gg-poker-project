import React from "react";
import Skateparkcard from "./SkateparkCard";

function BronxTab ({bronxParks}) {

    const cardDisplay = bronxParks.map((park)=>{
        return <Skateparkcard key={park.id} id={park.id} name={park.name} address={park.address} borough={park.borough} hours={park.hours}/>
    })

   
  return (
    <div className="BronxTab">
      {cardDisplay}
    </div>
  );
};

export default BronxTab;