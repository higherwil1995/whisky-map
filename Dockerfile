# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME whisky-map-venv

# # 設定 ENTRYPOINT
# ENTRYPOINT ["python", "-m", "uvicorn"]

# # Run main.py when the container launches
# CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]DockerfileCopy code

ENTRYPOINT ["uvicorn", "app.main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
