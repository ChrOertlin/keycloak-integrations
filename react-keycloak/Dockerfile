FROM node:20-alpine

WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose the port Vite uses
EXPOSE 3002

# Use the npm script to run Vite
CMD ["npm", "run", "dev", "--", "--host"]
