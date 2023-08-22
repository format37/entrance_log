FROM python:slim

# Set the working directory to /app
WORKDIR /app

RUN pip install --upgrade pip

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]