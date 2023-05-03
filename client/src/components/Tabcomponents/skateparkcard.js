import React, {useState} from "react";

import Reviews from "../Reviews";
import CustomPopup from "../CustomPopup";



function Skateparkcard ({id, name, address, borough, hours}) {

    const [visibility, setVisibility] = useState(false);
    const popupCloseHandler = (e) => {
        setVisibility(e);
      };

    
    
    
    return (
        <div>
        <br></br>
        <h3>{name}</h3>
        <p>Address: {address}</p>
        <p>Hours: {hours}</p>
        <button onClick={(e) => setVisibility(!visibility)}>Reviews</button>
        <CustomPopup
        onClose={popupCloseHandler}
        show={visibility}
        title="Reviews"
        >
        <Reviews skareparkId={id}/>
        </CustomPopup>
        </div>
    );
}

export default Skateparkcard;