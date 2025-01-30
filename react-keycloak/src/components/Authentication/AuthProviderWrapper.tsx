import { AuthProvider, AuthProviderProps } from "react-oidc-context";
import { useContext } from "react";
import AuthConfigContext from "./AuthConfigContext";
import { AuthConfigState } from "../../types/AuthConfigState";


const AuthProviderWrapper: React.FC<React.PropsWithChildren<{}>> = ({ children }) => {
  const authConfig: AuthConfigState = useContext(AuthConfigContext);

  const oidcConfig: AuthProviderProps = {
    authority: authConfig.authority,
    client_id: authConfig.clientId,
    redirect_uri: authConfig.redirectUrl,
    response_type: 'code',
    scope: 'openid profile email',
  };

  return (
    <AuthProvider {...oidcConfig}>
      {children}
    </AuthProvider>
  );
};

export default AuthProviderWrapper;