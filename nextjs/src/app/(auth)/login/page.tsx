"use client"

import Link from 'next/link'; <Link href={'home'}><button>Press</button></Link>
import { useState } from 'react';
import axiosInstance from '../../../config/axios';
import './login.css'

function LoginPage() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const submitHandler: React.FormEventHandler<HTMLFormElement> = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log(email)
        console.log(password)
        //login(email, password)
    };

    return (

        <div className='login-wrapper'>
            <form className='login-box' onSubmit={submitHandler}>
                <h1>Login</h1>
                <div className='form-set'>
                    <i className="fa-regular fa-at"></i>
                    <input
                        className='input-container'
                        type='email' id='email'
                        name='username'
                        placeholder='mail@exmaple.com'
                        pattern="\S+@\S+\.\S+"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div className='form-set'>
                    <i className="fa-solid fa-key"></i>
                    <input
                        className='input-container'
                        type='password'
                        placeholder='Enter Your Password'
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        minLength={6}
                        required
                    />
                </div>
                <button
                    type='submit'
                >
                    <span>Login</span>
                </button>
            </form>
        </div>


    )
}
export default LoginPage;
