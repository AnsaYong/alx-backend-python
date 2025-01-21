# Use the official Python image as a base
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY Requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r Requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the Django app runs on (default is 8000)
EXPOSE 8000

# Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
