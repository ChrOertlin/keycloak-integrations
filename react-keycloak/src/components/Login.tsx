import { useAuth } from "react-oidc-context";

function Login() {
    const auth = useAuth()

    if (auth.isLoading) {
        return <div>Loading...</div>
    }
  
    if (auth.error) {
        return <div>Oops... {auth.error.message}</div>
    }
  
    if (auth.isAuthenticated) {
        return (
            <div>
                Hi, {auth.user?.profile.name}{" "}
                <button onClick={auth.removeUser}>
                    Log out
                </button>
            </div>
        )
    }
    
    return (
    <div>
        <button onClick={() => auth.signinRedirect()}>Log in</button>
    </div>
  )
}

export default Login
