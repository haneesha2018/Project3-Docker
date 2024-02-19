# Use a minimal base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /home/app

# Copy the Python script and input text files into the container
COPY script.py IF.txt Limerick-1.txt /home/app/

# Set up a directory for output
RUN mkdir -p /home/output

# Entry point to execute the Python script
CMD ["python", "/home/app/script.py"]
