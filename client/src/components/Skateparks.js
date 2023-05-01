import React from "react";


import Tabs from "./Tabcomponents/Tabs";

function Skateparks ({skateparksdata}) {

   


    
    return (
        <div>
        <h1>Skateparks</h1>
        <div className="skateparks">
        <Tabs skateparkdata={skateparksdata}/>
        </div>
        </div>
    );
}

export default Skateparks;