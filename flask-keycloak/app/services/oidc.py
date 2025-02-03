from keycloak import KeycloakOpenID

# Configure Keycloak client
keycloak_openid = KeycloakOpenID(
    server_url="http://keycloak:8080",
    client_id="flask-client",
    realm_name="test-realm",
    client_secret_key="very-secret-password"
)
