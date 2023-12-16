"use client"

import Link from 'next/link';
import '../styles/authStyle.css'
import { loginAction } from '@/server-actions/auth/login';
import Button from '@/app/(app)/components/Button';
// import {logIn, logOut} from "@/redux/features/authSlice"
import { useDispatch } from 'react-redux';
import { AppDispatch } from '@/redux/store';
import { experimental_useFormState } from 'react-dom';
import { authActions } from '@/redux/features/authSlice';
function LoginPage() {


    // const [state, authAction] = experimental_useFormState(loginAction, initialState)

    // const dispatch = useDispatch<AppDispatch>();
    // const data = {email, password}
    // dispatch(authActions.fetchAuth(data));
    const buttonText = "Login"
    const dispatch = useDispatch<AppDispatch>();

    const ActionHandler = async (formData:FormData)=> {

        // const [state, authAction] = experimental_useFormState(loginAction, initialState)


        // const data = {formData.email, formData.password}
        dispatch(authActions.fetchAuth(formData));

        // const res = await loginAction(formData )
        // console.log(res)
    }

    return (
        <>
            <div className='login-wrapper'>

                <form className='login-box' action={ActionHandler}>
                    <h1>Login</h1>
                    <div className='form-set'>
                        <i className="fa-regular fa-at"></i>
                        <input
                            className='input-container'
                            type='email'
                            name='email'
                            placeholder='Enter Your Email.'
                            pattern="\S+@\S+\.\S+"
                            required
                        />
                    </div>
                    <div className='form-set'>
                        <i className="fa-solid fa-key"></i>
                        <input
                            className='input-container'
                            type='password'
                            name='password'
                            placeholder='Enter Your Password'
                            minLength={6}
                            required
                        />
                    </div>
                    <Button text={buttonText}/>

                </form>
                <p>Don't have an account ? </p>
                <Link className='link' href='/register'>
                    <span>SignUp</span>
                </Link>
            </div>
        </>

    )
}
export default LoginPage;
