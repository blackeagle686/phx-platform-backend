FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Set work directory to the Django project root
WORKDIR /app/project

# Collect static files (requires a dummy secret key if not set)
RUN python manage.py collectstatic --noinput

# The default command runs gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8089", "--workers", "3", "project.wsgi:application"]
