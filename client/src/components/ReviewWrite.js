import React, {useEffect, useState} from "react";
import { useFormik } from "formik"
import { Form } from "react-bootstrap"

function ReviewWrite ({skateparkId, setReviews, reviews}) {



    const formik = useFormik({
        initialValues: {
            review: ""
        },
        onSubmit: values => {
            // console.log(values)
            fetch(`/api/reviews/${skateparkId}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(values)
            })
            .then(res => res.json())
            .then(data => {
                // console.log(data)
                setReviews([...reviews, data])
            }
            )
        }
    })

    return (
        <Form onSubmit={formik.handleSubmit}>
            <label>Write a review below!</label>
            <br></br>
            <input type="text" name="review" placeholder="write review here!" value={formik.values.review} onChange={formik.handleChange}/>
            <br></br>
            <input type="submit" value="Submit"/>
        </Form>

    )
}

export default ReviewWrite;