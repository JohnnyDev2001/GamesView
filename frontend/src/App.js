import React, { Component } from "react";
import api from './Api';
import './App.css';
import HB from './HB.png'

class App extends Component{

  state = {
    games: [],
    uri: '',
  }
 
  async componentDidMount(){
    const response = await api.get("");

    this.setState({ games: response.data});
  }

  async componentDidUpdate(){
    const { uri } = this.state;
    const response = await api.get(uri);

    this.setState({ games: response.data});
  }

  render(){
    const { games, uri } = this.state;
    return(
      <>
      <div className="bar"><img src={HB}/></div>
      <label>
        <select value={uri} onChange={(e) => {
          const selectOption = e.target.value;
          this.setState({ uri: selectOption});
          
        }}>
          <option value="">Tudo</option>
          <option value="epic">Epic</option>
          <option value="steam">Steam</option>
        </select>
      </label>
      <div className="container">
        {console.log(games)}
        {games.map(game => (
          <div className="card">
            <div className="cardbody">
              <img src={game.imgLink}/>
              <h2>{game.title}</h2>
              <p>{game.price[1] != "" ? game.price[1] : "Valor não encontrado!"}</p>
            </div>
          </div>
        ))}
      </div>
      </>
    )
  }
}

export default App;
