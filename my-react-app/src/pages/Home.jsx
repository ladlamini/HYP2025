import React from 'react'
//import MenuSideBar from '../components/MenuSideBar'

function Home() {
     const [count, setCount] = useState(0)
  return (
    <>
    <MenuSideBar/>
      <h1>Welcome to an AI powered IDS</h1>
      <div className="card">
        
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