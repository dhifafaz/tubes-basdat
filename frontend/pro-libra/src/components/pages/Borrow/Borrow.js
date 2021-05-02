import React from 'react'
import {Link, Switch} from 'react-router-dom';
import {
  Col,
  Container,
  Row
} from 'react-bootstrap';
import './Borrow.css';
import '../BorrowCard/BorrowForm.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import RouteWithSubRoutes from '../../../utils/RouteWithSubRoutes';
import BorrowImage from 'C:\\Users\\HP\\yukiniyuk\\tubes-basdat\\frontend\\pro-libra\\src\\assets\\Images\\borrow-assets.svg';
const Borrow = ({routes})=> {
  return (

    <Container>
    <Row className="borrow-body"> 
    <Col md={3} xs={12} className="leftbar-column" >
      <div className="left-bar-menus">
          <ul>
            <div className="left-bar-menu">
              
              <Link to="/borrow/borrow-form" className="link-menu">
                <h2>
                Borrow Book
                </h2>
              </Link>
              
            </div>
            <div className="left-bar-menu">
              
              <Link to="/borrow/return-form" className="link-menu">
                <h2>Return Book</h2>
              </Link>
              
            </div>
          </ul>
        </div>  
      </Col>
      <Col md={9} xs={12} className="borrow-form-column">
      
      <Switch>
    {routes.map((route, i) => (
        <RouteWithSubRoutes key={i} {...route} />
    ))}
    <div className="main-display">
      <h1>Welcome use this page to borrow or return your book</h1>
        <img className="borrow-img" src={BorrowImage} alt="img"/>
      </div>
    </Switch>  
      </Col>
    </Row>
  </Container>
  
  )
}

export default Borrow;
