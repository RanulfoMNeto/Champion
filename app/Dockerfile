# Use the official Ubuntu base image
FROM ubuntu:latest

# Install Python, pip, and curl
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Set the virtual environment path
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the application code and requirements.txt into the container
COPY . /app

# Install the required Python packages
RUN pip install -r requirements.txt

# Make the script executable
RUN chmod +x script.sh

# Define the entry point
ENTRYPOINT ["./script.sh"]
