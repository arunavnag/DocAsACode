# Use a base image with Python installed
FROM python:3.9-slim

# Set build-time variables
ARG GIT_REPO_URL

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install the necessary Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Set an environment variable inside the container
ENV GIT_REPO_URL=${GIT_REPO_URL}

# Define a mount point for the volume
VOLUME ["/app/repo/local_repo"]

# Set the default command to run your application
CMD ["python", "main.py"]
