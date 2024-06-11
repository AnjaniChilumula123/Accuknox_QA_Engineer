# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary packages including netcat-openbsd
RUN apt-get update && apt-get install -y fortune-mod cowsay netcat-openbsd \
    && ln -s /usr/games/fortune /usr/local/bin/fortune \
    && ln -s /usr/games/cowsay /usr/local/bin/cowsay \
    && rm -rf /var/lib/apt/lists/*

# Make the wisecow.sh script executable
RUN chmod +x wisecow.sh

# Expose port 4499
EXPOSE 4499

# Run wisecow.sh when the container launches
CMD ["./wisecow.sh"]
