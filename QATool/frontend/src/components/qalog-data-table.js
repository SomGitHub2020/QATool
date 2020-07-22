import React, { Component } from 'react';
import { withRouter  } from 'react-router-dom';
import Modal from 'react-awesome-modal';
import axios from "axios";

class DataTable extends Component {
    
	constructor(props) {
        super(props)
        this.state = {
            visible : false,
            JiraFlag: true,
            value: 'JSON',
            qalogList: []
        }
        
    }
	 openModal() {
         this.setState({
             visible : true
         });
     }

     closeModal() {
         this.setState({
             visible : false
         });
     }
	render() {
        return (
            <tr>
                <td value="Open"  onClick={() => this.openModal()}>
                    {this.props.obj.SystemType}
                </td>
                <td value="Open"  onClick={() => this.openModal()}>
                    {this.props.obj.QALogID}
                </td>
                <td value="Open"  onClick={() => this.openModal()}>
                	{this.props.obj.QAConnID}
	            </td>
	            <td value="Open"  onClick={() => this.openModal()}>
	            	{this.props.obj.QACreatedDate}
	            </td>
	            <td value="Open"  onClick={() => this.openModal()}>
                	{this.props.obj.QALoggedDate}
                </td>
                <td value="Open"  onClick={() => this.openModal()}>
                {this.props.obj.JIRALogFlag}
                </td>
                <td> {this.SendToJIRA()} </td>
                <Modal  visible={this.state.visible}  width="600"  effect="fadeInUp">
					<div  className="Qalog">
						<h4>QALog</h4><br/>
					</div>
					<div className="model"> 
						<p>{this.ModalPopUp(this.props.obj)}</p><br/><br/>
					</div>
					<div className="centerize">
						<button style={{color: "red"}}  onClick={() => this.closeModal()}>Close</button>
					</div>
	            </Modal>
            </tr>
        );
    }//render ends
	
	SendToJIRA = item => {
		if(this.props.obj.JIRALogFlag === "RDY" || this.props.obj.JIRALogFlag === "SNT" )
    	return <button type="button" disabled={this.state.JiraFlag} onClick={() => this.JiraFlag(this.props.obj)}>Send To JIRA</button>;
        
    	else 
    		return <button type="button" disabled={!this.state.JiraFlag} onClick={() => this.JiraFlag(this.props.obj)}>Send To JIRA</button>;
//		 this.setState({JiraFlag: "RDY"});
//		 this.setState({JIRAvalue: !this.state.JIRAvalue});
      };
      JiraFlag = item => {
    	  this.setState({JiraFlag: false});
    	  var apiBaseUrl = "http://127.0.0.1:8000/api/qalogs/"+item.id+"/";
          var payload={
        		 "QALogID": item.QALogID,
      			"SystemType": item.SystemType,
      			"QAConnID": item.QAConnID,
      			"QACreatedDate": item.QACreatedDate,
      			"JIRALogFlag": "RDY",
      			"QALog": item.QALog,
                "QALoggedDate": item.QALoggedDate,
                "ObjectName": item.ObjectName,
                "ObjectPath": item.ObjectPath,
                "DevelopedBy": item.DevelopedBy  
          }
          axios.put(apiBaseUrl, payload)
          
          .catch(function (error) {
             
           console.log(error);
          });
          window.location.reload(false);
      }
      
	ModalPopUp = item => {
//    	if(this.state.value === "XML")
//    	{
    		return(item.QALog);
//    	}
//    	else
//    	{	
//    	var convert = require('xml-js');
//    	var options = {ignoreComment: true, alwaysChildren: true};
//    	var result = convert.xml2json(item.QALog, options); 
//    	 return (result); 
//    	}
    	   	
      };

      change = item => {
          this.setState({value: item.target.value});
      };
}//class ends
export default withRouter(DataTable);