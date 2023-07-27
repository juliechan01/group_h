'use client'

import React from 'react'
import Link from 'next/link'
import Image from 'next/image'

function page() {
	return (
		<div className='body-div'>
			<div className='nav-bar'>
				<div className='nav-bar-component'>
					<h1>yiip</h1>
					{/*Add map route later*/}
					<Link href="#">Map</Link>
					{/*Didn't quite understand this part, ask for elaboration later.*/}
					<Link href="#">I'm feeling lucky</Link>
				</div>

				<div className='nav-bar-component'>
					{/*Not totally sure what this button does yet?*/}
					<Link href="#">About</Link>
					{/*Made this into one button, since our login/register page is all in one.*/}
					<Link href="/welcome" className='sign-up-btn'>Sign up/Login</Link>
				</div>
			</div>

			{/*In future, find a way to populate this with 5 actual resturants from the DB.*/}
			<div className='restaurant-carousel'>
				<div className='restaurant'>
					<Link href='/1'> {/*Thought it'd be cool if clicking the image also worked the same as the see more button - Noah*/}
						<Image
							src={'/yiip-logo.png'}
							height={250}
							width={175}
							alt='Placeholder Restaurant Image'
						/>
					</Link>

					{/*This one actually goes somewhere!*/}
					<p>Test Place</p>
					<Link href='/1'>{`See More >>>`}</Link>
				</div>

				<div className='restaurant'>
					<Image
						src={'/yiip-logo.png'}
						height={250}
						width={175}
						alt='Placeholder Restaurant Image'
					/>

					<p>Restaurant Name</p>
					<Link href='#'>{`See More >>>`}</Link>
				</div>

				<div className='restaurant'>
					<Image
						src={'/yiip-logo.png'}
						height={250}
						width={175}
						alt='Placeholder Restaurant Image'
					/>

					<p>Restaurant Name</p>
					<Link href='#'>{`See More >>>`}</Link>
				</div>

				<div className='restaurant'>
					<Image
						src={'/yiip-logo.png'}
						height={250}
						width={175}
						alt='Placeholder Restaurant Image'
					/>

					<p>Restaurant Name</p>
					<Link href='#'>{`See More >>>`}</Link>
				</div>

				<div className='restaurant'>
					<Image
						src={'/yiip-logo.png'}
						height={250}
						width={175}
						alt='Placeholder Restaurant Image'
					/>

					<p>Restaurant Name</p>
					<Link href='#'>{`See More >>>`}</Link>
				</div>
			</div>

		</div>
	)
}

export default page