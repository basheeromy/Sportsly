"use client"

//import Link from 'next/link';<Link href={'home'}><button>Press</button></Link>
import React, { useEffect, useState } from 'react';
import axiosInstance from '../../../config/axios';

function LoginPage() {
    const [data, setData] = useState([]);

    useEffect(() => {
        axiosInstance.get('/api/list-product-item')
            .then((response) => {
                setData(response.data);

            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }, []);

    return (
        <div>
            {/* Render data from the GET request */}
            <h1>Hello from Register</h1>

            {
                <div>
                    {JSON.stringify(data)}
                </div>
            }

        </div>
    )
}
export default LoginPage;