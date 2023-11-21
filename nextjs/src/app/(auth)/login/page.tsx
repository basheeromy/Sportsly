"use client"

import Link from 'next/link';
import './login.css'
import { loginAction } from '@/server-actions/auth/login';
import Button from '@/app/(app)/components/Button';
function LoginPage() {


    // const [state, authAction] = experimental_useFormState(loginAction, initialState)

    // const dispatch = useDispatch<AppDispatch>();
    // const data = {email, password}
    //dispatch(authActions.fetchAuth(data));
    const buttonText = "Login"

    const ActionHandler = async (formData:FormData)=> {

        const res = await loginAction(formData )
        console.log(res)
    }

    return (
        <>
            <section className='titleWrapper'>
                <div className='sportsly'>
                    <span>S</span>portsly
                </div>
            </section>

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
                    <div className='form-set second'>
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
            </div>
        </>

    )
}
export default LoginPage;
