# Base image with Python environment
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application code and requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy remaining application files
COPY . .

# Expose port (if your application listens on a specific port)
EXPOSE 8000 

# Command to run the application
CMD [ "python", "src/app.py" ]