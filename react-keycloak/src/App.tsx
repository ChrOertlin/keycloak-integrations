import Header from './components/Header/Header';
import ProtectedComponent from './components/ProtectedComponent';

function App() {
  return (
    <div className='App'>
      <Header/>
    <div className="min-h-screen p-4 flex-col">
      <div className="mb-1 text-center">
        <h1 className="text-3xl font-bold underline">
          Welcome to the react-keycloak integration test app.
        </h1>
      </div>
      <div>
        <ProtectedComponent />
      </div>
    </div>
    </div>
  );
}

export default App;