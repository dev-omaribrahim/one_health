FROM python:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y gcc libpq-dev
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate 

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "one_health_project.wsgi:application"]
