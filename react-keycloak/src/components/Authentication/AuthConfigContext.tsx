import AuthConfigData from '../../auth-config.json';
import { AuthConfigState } from '../../types/AuthConfigState';
import { createContext } from 'react';


const AuthConfig: AuthConfigState = {
    authority: AuthConfigData.authority,
    clientId: AuthConfigData.clientId,
    redirectUrl: AuthConfigData.redirectUrl
}

const AuthConfigContext = createContext<AuthConfigState>(AuthConfig);

export default AuthConfigContext;
