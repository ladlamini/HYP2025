

//components imports
import MenuSideBar from './components/MenuSideBar.jsx'
//stuff so this pages works lol
import './App.css'
import './Index.css'
import {BrowserRouter as Router, Routes, Route, BrowserRouter} from "react-router-dom"
import {Link} from "react-router-dom"
//page imports
import Home from './pages/Home.jsx'
import DatasetSelection from './pages/DatasetSelection.jsx'
import Dashboard from './pages/Dashboard.jsx'
import Training from './pages/Training.jsx'
import Knowledge from './pages/Knowledge.jsx'


function App() {
return(
<div>
  
  <MenuSideBar/>

{/* Routes to the pages */}
<Routes>
   <Route path="/home" element={<Home />}></Route> 
   <Route path="/DatasetSelection" element ={<DatasetSelection />}></Route>
   <Route path="/Dashboard" element ={<Dashboard />}></Route>
   <Route path="/Training" element ={<Training />}></Route>
   <Route path="/Knowledge" element ={<Knowledge/>}></Route>
</Routes>
</div>
);

}

export default App
