import React, {useState} from 'react'
import {useNavigate} from 'react-router-dom'

import { useFormik } from "formik"
import * as yup from "yup"
import { Form } from "react-bootstrap"

function Authentication({updateUser}) {
    const [signUp, setSignUp] = useState(false)
    const [error, setError] = useState(false)
    const navigate = useNavigate()
  
    const handleClick = () => setSignUp((signUp) => !signUp)

    const formSchema = yup.object().shape({
      name: yup.string().required("Please enter a username"),
      email: yup.string().email()
    })
  
    const formik = useFormik({
      initialValues:{
        name:'',
        email:'',
        password:''
      },
      validationSchema:formSchema,
      onSubmit:(values) =>{
        fetch(signUp?'/signup':'/login',{
          method:"POST",
          headers:{
            "Content-Type":"application/json"
          },
          body: JSON.stringify(values)
        })
        .then(res => {
            if(res.ok){
                res.json().then(user => {
                    updateUser(user)
                    navigate('/skateparks')
                })
            }
            else {
                res.json().then(error => setError(error.message))
            }
        })
      }
    })
   
      return (
          <> 
          {Object.values(formik.errors).map(error => <h2 style={{color:'red'}}> {error}</h2>)}
            {error&&<h2 style={{color:'red'}}>{error}</h2>}
          <h2>Please Log in or Sign up!</h2>
          <h2>{signUp?'Already a member?':'Not a member?'}</h2>
          <button onClick={handleClick}>{signUp?'Log In!':'Register now!'}</button>
          <Form onSubmit={formik.handleSubmit}>
          <label>
            Username
            </label>
          <input type='text' name='name' value={formik.values.name} onChange={formik.handleChange} />
          <label>
           Password
           </label>
           <input type='password' name='password' value={formik.values.password} onChange={formik.handleChange} />
          {signUp&&(
            <>
            <label>
            Email
            </label>
            <input type='text' name='email' value={formik.values.email} onChange={formik.handleChange} />
            </>
          )}
          <input type='submit' value={signUp?'Sign Up!':'Log In!'} />
        </Form>
          </>
      )
  }
  
  export default Authentication