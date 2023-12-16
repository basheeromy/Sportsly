"use client"

import '../styles/authStyle.css'
import Link from 'next/link';
import Button from '@/app/(app)/components/Button';
import { registerAction } from '@/server-actions/auth/register';

function RegisterPage() {

    const buttonText = "Sign Up"

    const ActionHandler = async (formData:FormData)=> {
        const res = await registerAction(formData )
        console.log(res)
    }


    return (
        <>

            <div className='login-wrapper'>

                <form className='login-box' action={ActionHandler}>
                    <h1>SignUp</h1>
                    <div className='form-set'>
                        <i className="fa-regular fa-at"></i>
                        <input
                            className='input-container'
                            type='email'
                            name='email'
                            placeholder='Email ID'
                            pattern="\S+@\S+\.\S+"
                            required
                        />
                    </div>
                    <div className='form-set'>
                        <i className="fa-solid fa-mobile"></i>
                        <input
                            className='input-container'
                            type='tel'
                            name='mobile'
                            placeholder='Mobile Number'
                            pattern="^\+?[0-9]{1,3}-?[0-9]{3}-?[0-9]{3}-?[0-9]{4}$"
                            maxLength={14}
                            title="Please enter a valid phone number in the format +123-456-7890 or 123-456-7890"
                            required
                        />
                    </div>
                    <div className='form-set'>
                        <i className="fa-regular fa-user"></i>
                        <input
                            className='input-container'
                            type='text'
                            name='name'
                            placeholder='Name'
                            required
                        />
                    </div>
                    <div className='form-set second'>
                        <i className="fa-solid fa-key"></i>
                        <input
                            className='input-container'
                            type='password'
                            name='password'
                            placeholder='Password'
                            minLength={6}
                            required
                        />
                    </div>
                    <Button text={buttonText}/>

                </form>
                <p>Already have an account ? </p>
                <Link className='link' href='/login'>
                    <span>Login</span>
                </Link>

            </div>
        </>
    )
}
export default RegisterPage;