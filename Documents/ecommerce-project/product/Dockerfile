# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code and install dependencies
COPY . /app

# install flask
RUN pip install Flask 

# Expose the port the app runs on
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]
