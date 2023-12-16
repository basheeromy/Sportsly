import './authGlobals.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Script from 'next/script'
import { ReduxProvider } from '@/redux/provider'
import Link from 'next/link'


const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: "Sportsly",
  description: '',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (


    <html lang="en">

      <body>
          <Script
            src="https://kit.fontawesome.com/a978016096.js"
            crossOrigin="anonymous">
          </Script>
        <div className='Wrapper'>
          <Link className='sportsly' href='/'>
            <span>S</span>portsly
          </Link>

          <ReduxProvider> {children} </ReduxProvider>
          </div>
      </body>
    </html>

  )
}