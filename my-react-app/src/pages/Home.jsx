import React from 'react'
import MenuSideBar from '../components/MenuSideBar.jsx'
import { FaDropbox } from 'react-icons/fa';

function Home() {
     
  return (
    <>
    <MenuSideBar/>
      <h1>Welcome to an AI powered IDS</h1>
      
         {/* <MenuSideBar/> */}
      <div className="card">
      </div>
      <p className="read-the-docs">
        Select your dataset below
   <br/>
        <button >
          Dataset
        </button>
      </p>
    </>
  )
}

export default Home