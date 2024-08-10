# Use the official Ubuntu base image
FROM ubuntu:latest

# Install Python, pip, and curl
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Install BeautifulSoup4 in the virtual environment
RUN /opt/venv/bin/pip install beautifulsoup4

# Set the virtual environment path
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Make the script executable
RUN chmod +x script.sh

# Define the entry point
ENTRYPOINT ["./script.sh"]
