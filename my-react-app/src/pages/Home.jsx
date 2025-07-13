import React from 'react'
import MenuSideBar from '../components/MenuSideBar.jsx';

function Home() {
     
  
  return (
    <>
    <MenuSideBar/>
  {/* <Route path= "/Home" element={<Home/>}></Route> */}
      <h1>Welcome to an AI powered IDS</h1>
      
         {/* <MenuSideBar/> */}
      <div className="card">
        {/* <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button> */}
        {/* <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p> */}
      </div>
      <p className="read-the-docs">
        Select your dataset below
        <hr/>
        <button>
          Dataset
        </button>
      </p>
    </>
  )
}

export default Home