import React, {useState} from 'react';
import axios from 'axios'

function Training() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState('');
  const [loadingk, setLoadingk] = useState(false);
  const [resultk, setResultk] = useState(null);
  const [errork, setErrork] = useState(null);
  const [successk, setSuccessk] = useState('');


  const runMLServer = async () => {
    setLoading(true);
    setError(null);
    setResult(null);
    setSuccess('');

    try {
      const response = await axios.get('http://localhost:5000/runML');
      setResult(response.data);
      setSuccess('Model training completed successfully!');
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to run rf server');
    } finally {
      setLoading(false);
    }
  };

  const runMLkServer = async () => {
    setLoadingk(true);
    setErrork(null);
    setResultk(null);
    setSuccessk('');

    try {
      const response = await axios.get('http://localhost:5000/runMLk');
      setResultk(response.data);
      setSuccessk('Model training completed successfully!');
    } catch (err) {
      setErrork(err.response?.data?.error || 'Failed to run K means server');
    } finally {
      setLoadingk(false);
    }
  };

  // Helper function to format output 
  const formatOutput = (output) => {
    if (typeof output === 'object') {
      return JSON.stringify(output, null, 2);
    }
    return output;
  };

  // const closePopup = () => {
  //   setShowPopup(false);
  // };

//   return (
//     <div>  
//       CICIDS2017 Dataset 
//       <hr/>
//       <button onClick={runMLServer} disabled={loading}>
//         {loading ? 'Training in Progress...' : 'Train Supervised Model'}
//       </button>
      
//       {loading && (
//         <div className="loading">
//           <div className="spinner"></div>
//           <p>Training model... This may take a few minutes</p>
//         </div>
//       )}

//       {(result || error) && (
//         <div className="results-container">
//           <h3>Training Results:</h3>
          
//           {error && (
//             <div className="error-box">
//               <h4>Error:</h4>
//               <pre>{error}</pre>
//             </div>
//           )}


//           {success && (
//             <div className="success-message">
//               {success}
//             </div>
//           )}
//         </div>
//       )}
          
//       <br/> 
//       <br/>
      
//       <button onClick={runMLkServer} disabled={loadingk}>
//         {loadingk ? 'Training in Progress...' : 'Train Unsupervised Model'}
//       </button>
      
//       {loadingk && (
//         <div className="loading">
//           <div className="spinner"></div>
//           <p>Training model... This may take a few minutes</p>
//         </div>
//       )}

//       {(resultk || errork) && (
//         <div className="results-container">
//           <h3>Training Results:</h3>
          
//           {errork && (
//             <div className="error-box">
//               <h4>Error:</h4>
//               <pre>{errork}</pre>
//             </div>
//           )}

//           {successk && (
//             <div className="success-message">
//               {successk}
//             </div>
//           )}
//         </div>
//       )}
         
//       <br/>
//       <hr/>
//     </div>
//   );
// };
  return (
       <div className="home-container">
      {/* Sidebar */}
  

           <h1 className="home-title">Model Training</h1>


          {/* Detection Card */}
          <div className="card">
            <h2>Random Forest</h2>
            <p>Intrusion detection.</p>
              <button onClick={runMLServer} disabled={loading}>
             {loading ? 'Training in Progress...' : 'Train Supervised Model'}
              </button>
      
           {loading && (
            <div className="loading">
            <div className="spinner"></div>
            <p>Training model... This may take a few minutes</p>
            </div>
                  )}

             {(result || error) && (
            <div className="results-container">
          <h3>Training Results:</h3>
          
          {error && (
            <div className="error-box">
              <h4>Error:</h4>
              <pre>{error}</pre>
            </div>
          )}


          {success && (
            <div className="success-message">
              {success}
            </div>
          )}
        </div>
      )}
      </div>
          
<br/>
          {/* Detection Card */}
    <div className="card">
            <h2> K Means</h2>
         <p>Intrusion detection.</p>
                 
      <button onClick={runMLkServer} disabled={loadingk}>
        {loadingk ? 'Training in Progress...' : 'Train Unsupervised Model'}
      </button>
      
      {loadingk && (
        <div className="loading">
          <div className="spinner"></div>
          <p>Training model... This may take a few minutes</p>
        </div>
      )}

      {(resultk || errork) && (
        <div className="results-container">
          <h3>Training Results:</h3>
          
          {errork && (
            <div className="error-box">
              <h4>Error:</h4>
              <pre>{errork}</pre>
            </div>
          )}

          {successk && (
            <div className="success-message">
              {successk}
            </div>
          )}
            </div>
              )}
     </div>

     </div>
         
  )}

export default Training;