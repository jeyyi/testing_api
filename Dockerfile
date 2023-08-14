# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install system-level dependencies
# RUN apt-get update && apt-get install -y libgl1

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    pip install opencv-python-headless

# Copy the rest of the application files into the container
COPY . .

# Expose the port that your FastAPI app will run on
EXPOSE 8000

# Set the entrypoint command to run Hypercorn
CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8000"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
