'use client'

import React, { useEffect, useState } from 'react';
import Link from 'next-routes';
import { useRouter } from 'next/navigation';
import BusinessForm from '../components/BusinessForm';
import LogoutButton from '../components/LogoutButton';

const AddBusiness = () => {
    const [ biz, setBiz ] = useState([]);
    const [ errors, setErrors ] = useState({});
	const {push} = useRouter();


    const createBiz = (e) => {
        e.preventDefault;
        fetch('http://localhost:8080/api/business', {
            body: JSON.stringify(biz),
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(res => {
            console.log(res);
            if(res.status == 201){
                push('/')
            }
        })
        .catch(err => {
            alert('Errors detected! Check console for message!');
            console.log(err);
        })
    }

    return (
        <>
            <div>
                <h3>yiip</h3>
                <a href="">Map</a>
                <Link href="#">Account</Link>
                <LogoutButton />
            </div>

            <h1>New entry</h1>

            <BusinessForm onSubmitProp={ createBiz } initialBiz='' initialName='' initialAddress='' initialPhone='' initialHours='' initialService='' errors={errors} />
        </>
    )
}

export default AddBusiness;