import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { withRouter  } from 'react-router-dom';
import axios from 'axios';

class DataScheduler extends React.Component {


    constructor(props) {
        super(props)
        //this.state = { qaconnCollection: [] };
     }

     componentDidMount() {
        this.refreshList();
        setInterval(this.refreshList, 2500); // runs every 5 seconds.
        //this.renderDataTable();
        
     }
    
     refreshList = () => {
        axios
        //.get("http://127.0.0.1:8000/api/qaconfigs/")
        .get("http://9.220.9.130:50200/XMII/Illuminator?IsTesting=T&QueryTemplate=Default/Som/OCP_ConnPlants/ProductionOrder/SQL_GetShopOrderDetails&Content-Type=text/json&IllumLoginName=som&IllumLoginPassword=password@1")
        .then(res => this.updatetables(res))
        .catch(err => console.log(err));
     };

     updatetables = (data) => {
    
        //alert("Hello");
        console.log(data);
      };

      render() {
        return (
            <button type="submit" className="btn btn-primary btn-block" >Submit</button>
        );
    }//render ends

}//class ends

export default withRouter(DataScheduler);