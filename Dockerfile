# Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --root-user-action=ignore -r requirements.txt

# Copy the app code
COPY . .

# Default command to run the app
ENTRYPOINT ["python", "main.py"]
