'use client'
import React from 'react';
import Link from 'next/link';
import LogoutButton from '../components/LogoutButton';

function Profile() {
    // LOGIC BEHIND AUTHENTICATION
    const { user } = user({ redirectTo: '/welcome' });

    if(!user || user.isLoggedIn === false) {
        return "Loading..."
    }

    return (
        <>
            <div className='navbar'>
                <h3>yiip</h3>
                <a href="">Map</a>
                <Link href="/add">Add a new business</Link>
                <Link href="#">Account</Link>
                <LogoutButton />
            </div>

            <div className='header'>
                <h1>Name here</h1> // USER'S NAME IS HERE
                <h2>headline here</h2> // ONE LINE ABOUT USER HERE
                <h3>bio here</h3> // USER BIO HERE
            </div>

            <div className='socials'>
                <p>socials here</p> // MAY NEED A FORM HERE TO ACCEPT USER INPUTTING THEIR SOCIAL MEDIAS
            </div>
        </>
    )
}

export default Profile;