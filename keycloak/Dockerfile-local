# Use the specified Keycloak version as the base image
FROM quay.io/keycloak/keycloak:26.0.8

# Set environment variables for the admin user credentials
ENV KC_BOOTSTRAP_ADMIN_USERNAME=admin
ENV KC_BOOTSTRAP_ADMIN_PASSWORD=admin

# Directory for importing realms
WORKDIR /opt/keycloak/data/import

# Copy the realm configuration file into the container
COPY ./realm/test-realm.json /opt/keycloak/data/import/

# Expose the default Keycloak port
EXPOSE 8080

# Command to run Keycloak in development mode with realm import
ENTRYPOINT ["sh", "-c", "/opt/keycloak/bin/kc.sh start-dev --import-realm"]
