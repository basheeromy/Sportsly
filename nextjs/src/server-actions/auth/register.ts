'use server'

import axios from "axios";

export const registerAction = async (FormData: FormData): Promise<{ message: string }> => {

    // unpack data recieved from formSubmission

    const email = FormData.get('email') as string;
    const mobile = FormData.get('mobile') as string;
    const name = FormData.get('name') as string;
    const password = FormData.get('password') as string;

    try {
        const response = await axios.post(
            'http://app:8000/api/user/',
            {
                email,
                mobile,
                password,
                name,
            },
            {
                headers: {
                    "Content-Type": 'application/json'
                }
            }
        );

        return { message: "Successful" }


    } catch (error: any) {
        console.log(error.response.data)
        return { message: error.response?.data || 'Something went wrong.'}
    }
}