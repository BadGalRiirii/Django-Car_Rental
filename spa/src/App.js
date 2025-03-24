import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import { useEffect, useState } from 'react';

function App() {

  const [posts, setPosts] = useState([]);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    axios.get('http://localhost:8000/api/v1/post/')
      .then(response => {
        setPosts(response.data);
      })
      .catch(err => {
        console.error("Error fetching posts:", err);
        setError("Failed to fetch posts. Please try again"); // Fix 'SetError' typo
      });
  }, []);
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      {
        posts.map((obj, index) => <div key={index}>{obj.title}</div>)
      }
    </div>
  );
}

export default App;