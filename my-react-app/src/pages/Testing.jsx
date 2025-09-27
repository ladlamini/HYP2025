import React from 'react'

function Testing() {
  return (
       <div className="home-container">
      {/* Sidebar */}
  

        <h1 className="home-title">Model Testing</h1>


          {/* Detection Card */}
          <div className="card">
            <h2>Supervised ML: Random Forest</h2>
            <p>Start the AI-powered intrusion detection process.</p>
            <button>Test</button>
          </div>
<br/>
          {/* Detection Card */}
          <div className="card">
            <h2>Unsupervised ML: K Means</h2>
            <p>Start the AI-powered intrusion detection process.</p>
            <button>Test</button>
          </div>

        </div>
  )
}

export default Testing