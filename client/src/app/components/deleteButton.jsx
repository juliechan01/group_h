'use client'
import React from 'react'

function DeleteButton() {

    const deleteHandler = () => {
        //Make a call to the delete route on the server
        //Redirect to the root page
    }

    return (
        <button onClick={deleteHandler}>Delete</button>
    )
}

export default DeleteButton