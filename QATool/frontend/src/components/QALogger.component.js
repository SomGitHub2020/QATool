import React, { Component } from 'react'
import axios from "axios";
import DataTable from './qalog-data-table';

class QALogger extends Component {
    constructor(props) {
        super(props)
        this.state = {
            visible : false,
            SapMII:"",
            SapABAP:"",
            SapUI:"",
            dataMII: [],
            dataABAP: [],
            dataUI: [],
            qalogList: [],
            chkboxMII: false,
            chkboxABAP: false,
			chkboxUI:false,
			MIIlist: [],
			ABAPlist: [],
			UIlist: [],
			disabledMIIList: true,
			disabledABAPList: true,
			disabledUIList: true,
        }   
    }
    componentDidMount () {
		this.getDropDownData();
        this.getLoggerData();
	  }
	  
	getDropDownData(){
		axios
		.get("http://127.0.0.1:8000/api/qaconfigs/?systemtype=MII")
		.then(res => this.setState({ MIIlist: res.data }))
		.catch(err => console.log(err));

		axios
		.get("http://127.0.0.1:8000/api/qaconfigs/?systemtype=ABAP")
		.then(res => this.setState({ ABAPlist: res.data }))
		.catch(err => console.log(err));

		axios
		.get("http://127.0.0.1:8000/api/qaconfigs/?systemtype=UI5")
		.then(res => this.setState({ UIlist: res.data }))
		.catch(err => console.log(err));
	}
    
      renderDataTable() {  
    	  return this.state.qalogList.map((data, i) => {
    	        return <DataTable obj={data} key={i} />;
    	    });
    	  
    	 }
      
       changeMII = item => {
          this.setState({SapMII: item.target.value});
         
      };
      
      handleChangeChkMII = item => {
		  this.setState({chkboxMII:!this.state.chkboxMII});
		  
		  this.setState({disabledMIIList: !this.state.disabledMIIList});
		  
      };
      changeABAP = item => {
          this.setState({SapABAP: item.target.value});
      }; 
      handleChangeChkABAP = item => {
		  this.setState({chkboxABAP:!this.state.chkboxABAP});
		  
		  this.setState({disabledABAPList: !this.state.disabledABAPList});
      };
      changeUI = item => {
          this.setState({SapUI: item.target.value});
      };
      handleChangeChkUI = item => {
		  this.setState({chkboxUI:!this.state.chkboxUI});
		  
		  this.setState({disabledUIList: !this.state.disabledUIList});
	  };
	  
	  getLoggerData()
      {
    	  if(this.state.chkboxMII !==  false )
    	  {		
				axios.get('http://127.0.0.1:8000/api/qalogs/', {
				   params: {SystemType: "MII",
					    	QAConnID: this.state.SapMII
					    }
					  })
		        .then(res =>  this.setState({ dataMII: res.data }))
		        .then( () => {
		        	if(this.state.chkboxABAP === false && this.state.chkboxUI === false)
					{
						 this.setState({qalogList :this.state.dataMII});
					}
		        	
		        })
		        .catch(err => console.log(err)); 
	    	}
    	  if(this.state.chkboxABAP !==  false)
	  		{
	  			axios.get('http://127.0.0.1:8000/api/qalogs/?QAConnID', {
	  	    			    params: {
	  	    			    	SystemType: "ABAP",
	  	    			    	QAConnID: this.state.SapABAP
	  	    			    }
	  	    		})
	  	          .then(res => this.setState({ dataABAP: res.data }))
	  	          .then( () => {
		  	        	if(this.state.chkboxMII === true && this.state.chkboxUI === false)
			  			{	
			  				 this.setState({qalogList : this.state.dataABAP.concat(this.state.dataMII)});
			  			}
			  			if(this.state.chkboxMII === false && this.state.chkboxUI === false)
			  			{	
			  				 this.setState({qalogList :this.state.dataABAP});
			  			}
	  	          	})  
	  	          .catch(err => console.log(err));   
	  		}
	  		
			if(this.state.chkboxUI !==  false)
	  		{
	  			axios.get('http://127.0.0.1:8000/api/qalogs/?QAConnID', {
	  	    			    params: {SystemType: "UI5",
	  	    			    	QAConnID: this.state.SapUI
	  	    			    }
	  	    		})
	  	          .then(res => this.setState({ dataUI: res.data }))
	  	          .then( () => {
		  	        	if(this.state.chkboxMII === true && this.state.chkboxABAP === false)
			  			{	
			  				 this.setState({qalogList : this.state.dataUI.concat(this.state.dataMII)});
			  			}
			  			if(this.state.chkboxABAP === true && this.state.chkboxMII === false )
			  			{	
			  				 this.setState({qalogList : this.state.dataUI.concat(this.state.dataABAP)});
			  			}
			  			if(this.state.chkboxMII === true && this.state.chkboxABAP === true )
			  			{	
			  				this.state.dataUI = this.state.dataUI.concat(this.state.dataMII);
			  				this.setState({qalogList : this.state.dataUI.concat(this.state.dataABAP)});
			  			}
			  			if(this.state.chkboxABAP === false && this.state.chkboxMII === false)
			  			{	
			  				 this.setState({qalogList :this.state.dataUI});
			  			}
	  	          	})  
	  	          .catch(err => console.log(err));    
	  			
	  		}
			if(this.state.chkboxMII ===  false && this.state.chkboxABAP ===  false && this.state.chkboxUI ===  false)
			{
				axios
				.get("http://127.0.0.1:8000/api/qalogs/") 
				.then(res => this.setState({ qalogList: res.data }))
				.catch(err => console.log(err));
			}

    	};
		
		connnamehandler = (e) => {
			alert(e.target.value);
			this.setState({qaconnid:e.target.value});
		 };
    	
    render() { 
    	return (
            <div>
                <form onSubmit={this.handleSubmit}>
                <div className="App">
              </div>
                <div className="centerize">
                   <h3>QA Logging</h3>
                   <label>SAP MII</label>
				   <input type="checkbox" defaultChecked={this.state.chkboxMII} onChange={this.handleChangeChkMII}></input>
				   <label>&nbsp;&nbsp;</label>

				   {['qaconnid'].map(key => (
                     <select key={key} onChange={this.changeMII} disabled={this.state.disabledMIIList}>
                     <option value="">ALL</option>
                        {this.state.MIIlist.map(({ [key]: value }) => <option key={value}>{value}</option>)}
                     </select>
                  	))}





				   <label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
					<label>SAP ABAP</label>
					<input type="checkbox" defaultChecked={this.state.chkboxABAP} onChange={this.handleChangeChkABAP}></input>
					<label>&nbsp;&nbsp;</label>

					{['qaconnid'].map(key => (
                     <select key={key} onChange={this.changeABAP} disabled={this.state.disabledABAPList}>
                     <option value="">ALL</option>
                        {this.state.ABAPlist.map(({ [key]: value }) => <option key={value}>{value}</option>)}
                     </select>
                  	))}


					<label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
					<label>SAP UI5</label>	
					<input type="checkbox" defaultChecked={this.state.chkboxUI} onChange={this.handleChangeChkUI}></input>
					<label>&nbsp;&nbsp;</label>

					{['qaconnid'].map(key => (
                     <select key={key} onChange={this.changeUI} disabled={this.state.disabledUIList}>
                     <option value="">ALL</option>
                        {this.state.UIlist.map(({ [key]: value }) => <option key={value}>{value}</option>)}
                     </select>
                  	))}

					
					<br/>
                    <button type="button" onClick={() => this.getLoggerData()}>Filter</button><br/>
                </div>
                <div id="tableContainer">
					<table >
	                    <thead className="thead-dark">
	                        <tr>
	                            <td>QASystem</td>
	                            <td>QALogID</td>
	                            <td>QAConnID</td>
	                            <td>QACreatedDate</td>
	                            <td>QALoggedDate</td>
	                            <td>Status</td>
	                            <td></td>
	                        </tr>
	                    </thead>
	                    <tbody>
	                        {this.renderDataTable()}
	                    </tbody>
		                </table>
	             </div> 
	                <div className="centerize">
	                <button type="button"  onClick={() => this.getLoggerData()}>View in JIRA</button><br/>
	                </div>
                </form>
            </div>
            
        )
    }
}

export default QALogger
