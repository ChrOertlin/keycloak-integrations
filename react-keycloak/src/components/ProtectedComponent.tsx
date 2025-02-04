import { useAuth } from 'react-oidc-context';
import { useGetUser } from '../hooks/getUser';
import { useState } from 'react';

function ProtectedComponent() {
    const auth = useAuth();
    const fetchUser = useGetUser();
    const [user, setUser] = useState<any>(null);

    const handleGetUser = async () => {
        const fetchedUser = await fetchUser();
        setUser(fetchedUser);
    };

    if (auth.isAuthenticated) {
        return (
            <div className='flex flex-col justify-center items-center h-screen'>
                <div>
                    You are authenticated
                </div>
                <button
                    onClick={handleGetUser}
                    className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
                >
                    Get user
                </button>
                {user && (
                    <div className="mt-4">
                        <p>User: {user.user}</p>
                    </div>
                )}
            </div>
        );
    }

    return null;
}

export default ProtectedComponent;