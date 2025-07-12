import { useState } from 'react'
import React from 'react'
import {Link} from "react-router-dom"
import { FaBars } from 'react-icons/fa'
import Home from '../pages/Home';

function MenuSideBar() {
     // const [isOpen, setIsOpen] = useState(false);
        //const navigate = useNavigate();
  return (
    <>
      <div className='menubar'>
          <ul className='menu-items'>
                <a href="/home">Home</a>
                <a href="#">Upload Dataset</a>
                <a href="#">Training</a>
                <a href="#">Results</a>
                <a href="#">Dashboard</a>
                <a href="#">Knowledge</a>
          </ul>
      </div>
    </>
  );
};

export default MenuSideBar;

//futureme: When the model is finished trainign and has the best model, we then do a message box to say we now proceed to build the results of IDs