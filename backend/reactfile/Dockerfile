FROM node:16-alpine

# Set the working directory in the container
WORKDIR /backend

# Copy the current directory contents into the container at /frontend
COPY . /backend/

# Install dependencies
RUN npm install

# Expose port 3000 to the outside world
EXPOSE 3000

# Define the command to run the application
CMD ["npm","start"]