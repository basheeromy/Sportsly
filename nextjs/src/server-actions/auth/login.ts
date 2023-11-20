'use server'

import axios from "axios";
import {cookies} from 'next/headers'

export const loginAction = async (FormData: FormData): Promise<{ message: string }> => {

    // unpack data recieved from formSubmission

    const email = FormData.get('email') as string;
    const password = FormData.get('password') as string;

    try {
        const response = await axios.post(
            'http://app:8000/api/user/token/',
            {
                email,
                password
            },
            {
                headers: {
                    "Content-Type": 'application/json'
                }
            }
        );

        // Set cookies.
        
        cookies().set('access', response.data.access, {
            httpOnly: true,
            secure: process.env.NODE_ENV !== 'development',
            maxAge: 60 * 60 * 24 * 15, // 15 days
            sameSite: 'lax',
            path: '/',
        })
        return { message: "Successful" }


    } catch (error: any) {
        return { message: error.response?.data?.non_field_errors[0] || 'Something went wrong.'}
    }
}
