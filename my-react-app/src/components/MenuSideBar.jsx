import { useState } from 'react'
import React from 'react'
import {Link, Routes, Route} from "react-router-dom"
import { FaBars } from 'react-icons/fa'


function MenuSideBar() {
    
  return (
    <>
      <div className='menubar'>
          <ul className='menu-items'>
             <Link to="/home">Home</Link>
             <Link to="/datasetselection">Upload Dataset</Link> 
            <Link to="/training">Train the model</Link> 
            <Link to="/dashboard">Dashboard</Link> 
             <Link to="/knowledge">Knowledge</Link> 
          </ul>
      </div>
    </>
  )
}

export default MenuSideBar;

//futureme: When the model is finished trainign and has the best model, we then do a message box to say we now proceed to build the results of IDs