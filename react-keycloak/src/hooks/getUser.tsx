import axios from "axios";
import { useAuth } from "react-oidc-context";

export function useGetUser() {
    const auth = useAuth();
    
    const fetchUser = async () => {
        const token = auth.user?.access_token;
        console.log(`TOKEN: ${token}`);
        const url = "http://localhost:3001/users/get_user";
        const headers = { "Authorization": `Bearer ${token}` };
        console.log(`Making GET request to: ${url}`);
        console.log(`Headers:`, headers);
        try {
            const response = await axios.get(
                url, 
                { headers});
            return response.data;
        } catch (err) {
            console.error(err);
            return null;
        }
    };
    return fetchUser;
}