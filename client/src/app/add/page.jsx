import React, { useEffect, useState } from 'react';
import Link from 'next-routes';
import BusinessForm from '../components/BusinessForm';
import LogoutButton from '../components/LogoutButton';
import CancelButton from '../components/CancelButton';

const AddBusiness = () => {
    const [ biz, setBiz ] = useState([]);
    const [ errors, setErrors ] = useState({});

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