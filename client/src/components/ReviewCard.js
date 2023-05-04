import React, {useEffect, useState} from "react";

function ReviewCard ({reviewData}) {
    
    const iReview = reviewData.map((review) => {
        return (
        <div>
        <br></br>    
        <p>{review.review}</p>
        </div>)
        
    })
        return (
            <div>
                {iReview}
            </div>
        );
    }

export default ReviewCard;