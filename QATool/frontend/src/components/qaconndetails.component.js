import React, { Component } from "react";
import axios from 'axios';
import DataTable from './data-table';

export default class MyTable extends React.Component {


constructor(props) {
    super(props)
    this.state = { qaconnCollection: [],
      defaulttriggerrate: "60", };
 }



 componentDidMount() {
    this.refreshList();
    setInterval(this.refreshList, 2500); // runs every 5 seconds.
    //this.renderDataTable();
    
 }

 refreshList = () => {
    axios
    .get("http://127.0.0.1:8000/api/qaconfigs/")
    .then(res => this.setState({ qaconnCollection: res.data }))
    .catch(err => console.log(err));
 };

 renderDataTable() {
     //alert("1");
    return this.state.qaconnCollection.map((data, i) => {
        return <DataTable obj={data} key={i} />;
    });
 }

  render() {
    
    return (
        <div>
           <h1 id='title'>QA System Connections</h1>
           <button  className="btn btn-primary btn-block" onClick={() => this.goToConfig()}>Add QA Connection</button>
           <div>
              <table>
                 <tr>
                    <td>
                    <label>Trigger Rate (in Seconds)</label></td><td>
                    <input type="number" id="triggerfieldid" className="form-control" value={this.state.defaulttriggerrate} maxLength={3}  onChange={this.triggerratehandler} placeholder="Trigger Rate" />
                  </td>
                  </tr>
               </table>
            </div>
           <table id='students'>
              <thead>
                 <tr>
                    <td>QA Conn ID</td>
                    <td>System Type</td>
                    <td>IP Address</td>
                    <td>Port</td>
                    <td>Admin User</td>
                    <td>Admin Password</td>
                    <td>System ID</td>
                    <td>Client</td>
                    <td>Github URL</td>
                    <td id="trigger">Trigger UOM</td>
                    <td id="trigger">Trigger Rate</td>
                 </tr>
              </thead>
              <tbody>
                 {this.renderDataTable()}
              </tbody>
           </table>
        </div>
     )


  }//render ends

  goToConfig = () => {
    
   this.props.history.push("/qaconfig");
 };
}//class ends
