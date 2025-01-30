import Login from './components/Login';
import ProtectedComponent from './components/ProtectedComponent';


function App() {
  return (
    <div className="App">
      <div className='container center'>
        <Login />
        <ProtectedComponent />
      </div>
    </div>
  );
}

export default App;