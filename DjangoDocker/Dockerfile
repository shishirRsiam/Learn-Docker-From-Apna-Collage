FROM python:3.9

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
