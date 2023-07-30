'use client'
import React, { useState } from 'react';
import Image from 'next/image'
import Link from 'next/link';
import { useRouter } from 'next/navigation'

function Welcome() {

	const {push} = useRouter()
	const [newUser, setNewUser] = useState({
		firstName: "",
		lastName: "",
		email: "",
		password: "",
		confirmPassword: "",
		birthday: ""
	})
	const [loginUser, setLoginUser] = useState({
		email: "",
		password: ""
	})

	const addContainerClassHandler = (e) => {
		e.preventDefault()
		document.getElementById('container').classList.add("register-mode")
	}

	const removeContainerClassHandler = (e) => {
		e.preventDefault()
		document.getElementById('container').classList.remove("register-mode")
	}

	const newUserChangeHandler = e => {
		setNewUser({ ...newUser, [e.target.name]: e.target.value })
	}

	const createUserHandler = (e) => {
		e.preventDefault()
		fetch('http://localhost:8080/api/user', {
			body: JSON.stringify(newUser),
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(res => {
				console.log(res)
				if(res.status === 201){
					push('/')
				}
			})
			.catch(err => {
				alert('Errors detected! Check console for message!')
				console.log(err)
			})

	}

	return (
		<div style={{ position: 'relative' }}>
			<Image
				src='/background.jpg'
				alt='background'
				fill={true}
			/>
			<div className='container' id='container'>
				<div className='forms-container'>
					<div className='login-and-register'>
						<form className='login'>
							<h2 className='title'>Log in</h2>
							<div className='input-field'>
								<label>
									Email:
									<input type='text' id='email' name='email'></input>
								</label>
							</div>

							<div className='input-field'>
								<label>
									Password:
									<input type='password' id='password' name='password'></input>
								</label>
							</div>

							<button className='form-button'>Login</button>
						</form>

						<form className='register' onSubmit={createUserHandler}>
							<h2 className='title'>Register</h2>

							<div className='input-field'>
								<label>
									First Name:
									<input type='text' id='firstName' name='firstName' onChange={newUserChangeHandler}></input>
								</label>
							</div>

							<div className='input-field'>
								<label>
									Last Name:
									<input type='text' id='lastName' name='lastName' onChange={newUserChangeHandler}></input>
								</label>
							</div>

							<div className='input-field'>
								<label>
									Email:
									<input type='text' id='email' name='email' onChange={newUserChangeHandler}></input>
								</label>
							</div>

							<div className='input-field'>
								<label>
									Password:
									<input type='password' id='password' name='password' onChange={newUserChangeHandler}></input>
								</label>
							</div>

							<div className='input-field'>
								<label>
									Confirm Password:
									<input type='password' id='confirmPassword' name='confirmPassword' onChange={newUserChangeHandler}></input>
								</label>
							</div>

							<div className='input-field'>
								<label>
									Date of Birth:
									<input type='date' id='birthday' name='birthday' onChange={newUserChangeHandler}></input>
								</label>
							</div>

							<button className='form-button'>Register</button>
						</form>
					</div>
				</div>

				<div className='panels-container'>
					<div className='panel left-panel'>
						<div className='content'>
							<Link href="/" className='logo'>yiip</Link>
							<p>Let's create more memorable moments together.</p>
							<p>New here?</p>
							<button className='form-button transparent' id='register-button' onClick={addContainerClassHandler}>Register</button>
						</div>
					</div>
					<div className='panel right-panel'>
						<div className='content'>
							<Link href="/" className='logo'>yiip</Link>
							<p>Don't miss out on another experience. Sign up today.</p>
							<p>Already Registered?</p>
							<button className='form-button transparent' id='login-button' onClick={removeContainerClassHandler}>Login</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	)
}

export default Welcome;