import axios from "axios";
import { useAuth } from "react-oidc-context";

export function useGetUser() {
    const auth = useAuth();
    const token = auth.user?.access_token;
    const fetchUser = async () => {
        try {
            const response = await axios.get(
                "http://localhost:3001/users/get_user", 
                { headers: {"Authorization" : `Bearer ${token}`} });
            return response.data;
        } catch (err) {
            console.error(err);
            return null;
        }
    };
    return fetchUser;
}