import React, {useEffect, useState} from "react";
import ReviewCard from "./ReviewCard";
import ReviewWrite from "./ReviewWrite";


function Reviews ({skareparkId}) {

    const [reviews, setReviews] = useState([]);
    
    useEffect(() => {
        fetch(`/api/reviews/${skareparkId}`)
            .then(res => res.json())
            .then(data => {
                setReviews(data);
                // console.log(data)
            })
    }, [])

    return (
        <div>
        <p>Skatepark ID:{skareparkId}</p>
        <ReviewCard reviewData={reviews}/>
        <br></br>
        <ReviewWrite skateparkId={skareparkId} setReviews={setReviews} reviews={reviews}/>
        </div>
    );
}

export default Reviews;