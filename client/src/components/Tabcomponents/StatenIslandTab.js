import React, { createContext } from "react";
import Skateparkcard from "./SkateparkCard";

function StatenIslandTab ({statenislandParks}) {

    const cardDisplay = statenislandParks.map((park)=>{
        return <Skateparkcard key={park.id} name={park.name} address={park.address} borough={park.borough} hours={park.hours}/>
    })

  return (
    <div className="StatenIslandTab">
      {cardDisplay}
    </div>
  );
};

export default StatenIslandTab;