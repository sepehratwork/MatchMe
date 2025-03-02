# Dockerfile
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install pip -U
RUN pip install --no-cache-dir -r requirements.txt -U

# Copy the rest of your application code
COPY . .

# Expose the port that the gRPC server listens on
EXPOSE 50051

# Set the default command to run the gRPC server
CMD ["python", "server.py"]
