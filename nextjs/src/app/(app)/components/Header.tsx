import React from 'react'
import Link from 'next/link'
import './styles/header.css'

const Header = () => {
  return (
    <div className='header-wrapper'>
        <div className='sportsly'>
            <span>S</span>portsly
        </div>
        <div className='link-wrapper'>
            <Link className='link' href='/'>
                <span>SHOP ALL</span>
            </Link>
            <Link className='link' href='/'>
                <span>MEN</span>
            </Link>
            <Link className='link' href='/'>
                <span>WOMEN</span>
            </Link>
            <Link className='link' href='/'>
                <span>PACK & GEAR</span>
            </Link>
            <Link className='link' href='/'>
                <span>TOP DEALS</span>
            </Link>
            <div className='search-wrapper'>
                <i className="fa-solid fa-magnifying-glass"></i>
                <input type="text" />
            </div>

            <Link className='cart' href='/'>
            <i className="fa-solid fa-cart-shopping" ></i>
            </Link>

            <Link className='cart' href='/login'>
            <i className="fa-solid fa-user"></i>
            </Link>

        </div>
        <button className="hamburger">
            <span className="bar"></span>
            <span className="bar"></span>
            <span className="bar"></span>
        </button>



    </div>
  )
}

export default Header