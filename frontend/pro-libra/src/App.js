import React from 'react';
import './App.css';
import {BrowserRouter as Router, Switch} from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import routes from './Routes';
import RouteWithSubRoutes from './utils/RouteWithSubRoutes';
import Home from './components/pages/Home/Home';
import Footer from './components/Footer/Footer'
function App() {
  return (
    <Router >
      <Navbar/>
      <Switch >
        {routes.map((route, i) => (
          <RouteWithSubRoutes key={i} {...route}/>
        ))}
        <Home/>
      </Switch>
      <Footer/>
    </Router>  
  );
}

export default App;