# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for Whisper)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy Whisper repository files
COPY . .

# Install Python dependencies
RUN pip install -U openai-whisper
RUN pip install fastapi uvicorn
RUN pip install python-multipart

# Expose the port for the HTTP API
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]