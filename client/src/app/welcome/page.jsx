'use client'
import React from 'react';
import Image from 'next/image'
import Link from 'next/link';

function Welcome() {
	const addContainerClassHandler = (e) => {
		e.preventDefault()
		document.getElementById('container').classList.add("register-mode")
	}

	const removeContainerClassHandler = (e) => {
		e.preventDefault()
		document.getElementById('container').classList.remove("register-mode")
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

						<form className='register'>
							<h2 className='title'>Register</h2>

							<div className='input-field'>
								<label>
									First Name:
									<input type='text' id='first_name' name='first_name'></input>
								</label>
							</div>

							<div className='input-field'>
								<label>
									Last Name:
									<input type='text' id='last_name' name='last_name'></input>
								</label>
							</div>

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

							<div className='input-field'>
								<label>
									Date of Birth:
									<input type='date' id='birthday' name='birthday'></input>
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