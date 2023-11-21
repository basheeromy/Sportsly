import React from 'react'
import './styles/button.css'
// {text.text[0]}
const Button = (text:any) => {
  return (
      <div className='buttonWrapper'>
          <button
              type='submit'
          >
              <span>{text.text}</span>
          </button>
      </div>

  )
}

export default Button