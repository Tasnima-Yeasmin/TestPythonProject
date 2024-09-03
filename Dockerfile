FROM python:3.8.10

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 3000

WORKDIR /app/src

# Run the application
CMD ["python", "main.py"]
