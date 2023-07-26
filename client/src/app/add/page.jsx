'use client'
import React, { useState } from 'react'

function page() {

    const [newBusiness, setNewBusiness] = useState({})

    const onChangeHandler = e => {
        setNewBusiness({...newBusiness, [e.target.name]: e.target.value})
    }

    const submitHandler = e => {
        e.preventDefault()
        //Add logic to submit to the DB
        //Add redirect to the homepage after submitting
    }

    return (
        <div className='add-business'>
            <h1>Add a new Business</h1>

            <form method='post' onSubmit={submitHandler}>
                <div>
                    <label>
                        Business Type:
                        <input type="text" id='type' name='type' onChange={onChangeHandler}/>
                    </label>
                </div>

                <div>
                    <label>
                        Business Name:
                        <input type="text" id='name' name='name' onChange={onChangeHandler}/>
                    </label>
                </div>

                <div>
                    <label>
                        Business Address:
                        <input type="text" id='address' name='address' onChange={onChangeHandler}/>
                    </label>
                </div>

                <div>
                    <label>
                        Business Phone Number:
                        <input type="text" id='phone_number' name='phone_number' onChange={onChangeHandler}/>
                    </label>
                </div>

                <div>
                    <label>
                        Business Hours:
                        <input type="text" id='business_hours' name='business_hours' onChange={onChangeHandler}/>
                    </label>
                </div>

                <button>Add Business</button>
            </form>
        </div>
    )
}

export default page