import { useAuth } from "react-oidc-context";

function Login() {
    const auth = useAuth();

    if (auth.isLoading) {
        return <div>Loading...</div>;
    }

    if (auth.error) {
        return <div>Oops... {auth.error.message}</div>;
    }

    if (auth.isAuthenticated) {
        return (
            <div className="justify-center items-center ">
                <div>
                    Hi, {auth.user?.profile.name}{" "}
                    <button
                        onClick={auth.removeUser}
                        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
                    >
                        Log out
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div className="justify-center items-center ">
            <button
                onClick={() => auth.signinRedirect()}
                className="px-4 py-2 bg-blue-500 text-white rounded"
            >
                Log in
            </button>
        </div>
    );
}

export default Login;