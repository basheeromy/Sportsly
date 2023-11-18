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
                <span>WONEN</span>
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

        </div>


    </div>
  )
}

export default Header