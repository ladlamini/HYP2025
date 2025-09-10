import React from 'react'
import MenuSideBar from '../components/MenuSideBar.jsx'
import { FaDropbox } from 'react-icons/fa';
import '../Index.css'

function Home() {  
  return (
    <>
    <MenuSideBar/>   
      <h1>AI powered IDS with Visualisation</h1>
      
         {/* <MenuSideBar/> */}
      <div className="card">
      </div>
      <p className="title"> 
        {/* <button >
          Select a Dataset
        </button> */}
      </p>

    </>
  )
}

export default Home