'use client'
import Link from 'next/link'
import React, { useEffect, useState } from 'react'

function page() {

    //Dummy Data just for testing, will replace with proper API call
    const [currentBusiness, setCurrentBusiness] = useState({
        name: "Test Place",
        type: "Test",
        address: "101 Test Road",
        phone_number: "(555) 555-5555",
        business_hours: "Whenever we feel like it."
    })

    return (
        <div>
            {/*Styling on this is VERY temporary, and just for my own use. Feel free to remove and use something better. and preferable not inline - Noah*/}
            <Link href='/' className='logo' style={{color: `white`, width: `10%`}}>yiip</Link>
            <div className='details-page'>
                <h1>{currentBusiness.name}</h1>
                <p>Business Type: {currentBusiness.type}</p>
                <p>Business Address: {currentBusiness.address}</p>
                <p>Business Phone #: {currentBusiness.phone_number}</p>
                <p>Business Hours: {currentBusiness.business_hours}</p>
            </div>
        </div>
    )
}

export default page