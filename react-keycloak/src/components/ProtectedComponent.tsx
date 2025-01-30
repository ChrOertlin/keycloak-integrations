import { useAuth } from 'react-oidc-context';

function ProtectedComponent() {
    const auth = useAuth()
  if (auth.isAuthenticated) {
    return (
      <div>
        <h1>You are authenticated</h1>
      </div>
    );
  }
}

export default ProtectedComponent
