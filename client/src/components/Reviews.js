import React, {useEffect, useState} from "react";



function Reviews ({skareparkId}) {

    const [reviews, setReviews] = useState([]);
    

   



    useEffect(() => {
        fetch(`/api/reviews/${skareparkId}`)
            .then(res => res.json())
            .then(data => {
                setReviews(data);
                console.log(data)
            })
    }, [])

    

    return (
        <div>
        

        <p>Review body</p>
        <p>test</p>
      
        <p>Skatepark ID:{skareparkId}</p>
        </div>
    );
}

export default Reviews;