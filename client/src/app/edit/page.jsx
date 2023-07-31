'use client'

import React, { useEffect, useState } from 'react';
import Link from 'next-routes';
import BusinessForm from '../components/BusinessForm';
import LogoutButton from '../components/LogoutButton';
import CancelButton from '../components/CancelButton';
import DeleteButton from '../components/deleteButton';

const EditBusiness = () => {
    const { id } = useParams(); // PLEASE CHANGE NAME TO ID OF BUSINESS OBJECT NOT USER OBJECT; ALSO NOT SURE WHAT IS NEXT.JS EQUIVALENT TO useParams SINCE REACT-ROUTER-DOM DOESN'T APPLY TO NEXTJS
    const [biz, setBiz] = useState({});
    const [loaded, setLoaded] = useState(false);
    const [errors, setErrors] = useState({});

    const removeFromDom = () => {
        setBiz();
    }

    return (
        <>
            <div className='navbar'>
                <h3>yiip</h3>
                <a href="">Map</a>
                <Link href="#">Account</Link>
                <LogoutButton />
            </div>

            <h1>Edit {biz.name}</h1>

            {
                loaded &&
                <div>
                    <BusinessForm createBiz={updateBiz} initialBiz={biz.biz} initialName={biz.name} initialAddress={biz.address} initialPhone={biz.phone} initialHours={biz.hours} initialService={biz.service} errors={errors} />
                </div>
            }
            <DeleteButton bizId={biz._id} successCallback={() => removeFromDom(biz._id)} />
        </>
    )
}

export default EditBusiness;