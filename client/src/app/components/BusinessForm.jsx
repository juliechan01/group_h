import React, { useState } from 'react';
import CancelButton from './CancelButton';

const BusinessForm = (props) => {
    const { initialBiz, initialName, initialAddress, initialPhone, initialHours, initialService, createBiz, errors } = props;
    const [ biz, setBiz ] = useState(initialBiz);
    const [ name, setName ] = useState(initialName);
    const [ address, setAddress ] = useState(initialAddress);
    const [ phone, setPhone ] = useState(initialPhone);
    const [ hours, setHours ] = useState(initialHours);
    const [ service, setService ] = useState(initialService);

    const onSubmitHandler = async(e) => {
        e.preventDefault();
        try {
            const updatedInfo = await createBiz({ biz, name, address, phone, hours, service });
            onInfoUpdate(updatedInfo);
        }
        catch(error) {
            console.log(error);
        };
        setBiz('');
    };

    return (
        <div className='container'>
            <div className='form-control'>
                <form onSubmit = {onSubmitHandler}>
                    <>
                        <div className='col mt-3'>
                            <label>What type of business are you planning to add?</label>
                            <input type="text" className={`form-control ${errors.biz && 'is-invalid'}`} name='biz' value={biz} placeholder='Restaurant' onChange={(e) => setBiz(e.target.value)} />
                            { errors.biz &&
                                <p className='text-danger'>{errors.biz.message}</p>
                            }
                        </div>

                        <div className='col mt-3'>
                            <label>What's the name of the business?</label>
                            <input type="text" className={`form-control ${errors.name && 'is-invalid'}`} name='name' value={name} placeholder='Buffalo Wild Wings' onChange={(e) => setName(e.target.value)} />
                            { errors.name &&
                                <p className='text-danger'>{errors.name.message}</p>
                            }
                        </div>

                        <div className='col mt-3'>
                            <label>Where is this business located?</label>
                            <input type="text" className={`form-control ${errors.address && 'is-invalid'}`} name='address' value={address} placeholder='20 City Blvd E #901, Orange, CA' onChange={(e) => setAddress(e.target.value)} />
                            { errors.address &&
                                <p className='text-danger'>{errors.address.message}</p>
                            }
                        </div>

                        <div className='col mt-3'>
                            <label>What's the phone number of this business?</label>
                            <input type="text" className={`form-control ${errors.phone && 'is-invalid'}`} name='phone' value={phone} placeholder='657-345-0987' onChange={(e) => setPhone(e.target.value)} />
                            { errors.phone &&
                                <p className='text-danger'>{errors.phone.message}</p>
                            }
                        </div>

                        <div className='col mt-3'>
                            <label>What's this business's operating hours?</label>
                            <input type="text" className={`form-control ${errors.hours && 'is-invalid'}`} name='hours' value={hours} placeholder='10 AM - 8 PM' onChange={(e) => setHours(e.target.value)} />
                            { errors.hours &&
                                <p className='text-danger'>{errors.hours.message}</p>
                            }
                        </div>

                        <div className='col mt-3'>
                            <label>What type(s) of service(s) does this business provide? If it's a restaurant, please describe the cuisine they specialize in.</label>
                            <textarea className={`form-control ${errors.service && 'is-invalid'}`} name='service' value={service} placeholder='Type your description here...' onChange={(e) => setService(e.target.value)} />
                            { errors.service &&
                                <p className='text-danger'>{errors.service.message}</p>
                            }
                        </div>

                        <div className='buttons'>
                            <button type='submit' className='bg-[#B5C9C3] rounded-md p-2 mr-3'>Submit 💾</button>
                        </div>
                    </>
                </form>
                <Link to={'/profile'}>Cancel</Link>
            </div>
        </div>
    )

}

export default BusinessForm;