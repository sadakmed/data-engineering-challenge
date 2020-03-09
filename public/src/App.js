import React from 'react';
import axios from 'axios'
import { render } from 'react-dom';
import './App.css'


class App extends React.Component{
  constructor(props){
    super(props)
    this.state={
      author:[],
      tag:[],
      articles:[],
      page:[],
    }
  }


componentDidMount(){
  axios.get("http://127.0.0.1:5000/api/v1/news")
  .then(res=>{this.setState({articles:res.data})})

  axios.get("http://127.0.0.1:5000/api/v1/news/author")
  .then(res=>{this.setState({author:res.data.authors})})

  axios.get("http://127.0.0.1:5000/api/v1/news/tag")
  .then(res=>{this.setState({tag:res.data.tags})})
}


submit = (e) => {
              e.preventDefault()
              let tag = document.querySelector('#tag').value
              let author = document.querySelector('#author').value
              let keyword = document.querySelector('#keyword').value
              axios.get('http://127.0.0.1:5000/api/v1/news',{params:{ headline : keyword,
                                                                          tag : tag,
                                                                        author : author }})
                  .then( res => {this.setState(
                    { articles:res.data})
                    })
        }

browse = (e,id) => {
  e.preventDefault()
  axios.get("http://127.0.0.1:5000/api/v1/news/"+id)
  .then(res=>{this.setState({page:res.data})});

}




render() {
  return (
    <div className="App">
      <nav className="navbar navbar-default">
  <div className="container-fluid">
    <div className="navbar-header">
        
                  <div className="col-md-12 col-md-offset-4" style={{marginTop:'10px'}} >

                        <form className="form-inline mr-auto" onSubmit={e=>this.submit(e) }>
                          <input style={{marginRight:'5px'}}  className="form-control" type="text" id="keyword" placeholder="keywords" aria-label="Search"  />
                          
                          <select className="form-control"  style={{marginRight:'5px'}} id="tag"    >
                                <option value="" >Tag</option>
                                
                                {this.state.tag.map(a=> { return (
                                  <option value={a}>{a}</option>

                                )})}
                          </select>

                          <select className="form-control" style={{marginRight:'5px'}}  id="author"   >
                                <option value="" >Author</option>
                                {this.state.author.map(a=> { return (
                                  <option value={a}>{a}</option>

                                )})}    
                          </select>
                          
                          <button className="btn btn-mdb-color btn-rounded btn-sm my-0 ml-sm-2">Search</button>
                        </form>
                  </div>

      </div>
      </div>
      </nav>
      


                  <div className="container">
                          <div className="row" >
                                  <div className="col-sm-6">
                                  <div className="scroll-div">
                                  <table className="table table-bordered table-fixed text-center">
                                    <thead >
                                      <tr >
                                        <th className="text-center" >Headline</th>
                                        <th className="text-center" >Topic</th>
                                        <th className="text-center" >Author</th>
                                        <th  ></th>
                                      </tr>
                                    </thead>
                                    <tbody>
                                      {this.state.articles.map((art,i)=> {return (
                                            <tr  key={i}>
                                            <td><a href={art.url}>{i}. {art.headline}</a></td>
                                            <td>{art.tag}</td>
                                            <td>{art.authors[0]}</td>
                                            <td><a   onClick={(event)=>{event.preventDefault();this.browse(event,art._id.$oid);event.preventDefault()} }> Show </a></td>
                                            </tr>
                                      )})}
                                    </tbody>
                                  </table>

                                  </div>
                                  </div>
                                  <div className="col-sm-6">
                                      {this.state.page.map(pa=> {return (
                                            <div className="panel panel-default">
                                                  <div className="panel-heading">
                                                       <a href= {pa.url} >  <h3 className="panel-title text-center">{pa.headline}</h3></a>
                                                  </div>
                                                  <div className="panel-body">
                                                       
                                                  {pa.article.map(part=> {return (
                                                       
                                                      <p>  {part} </p>
                                                        
                                                        
                                                        )})}
                                                  </div>
                                            </div>
                                      )})}
                                  </div>
                          </div>
                  </div>
          </div>
     
  
  );
}

}


export default App;
