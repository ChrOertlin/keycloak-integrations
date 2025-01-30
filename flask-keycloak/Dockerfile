# Use Python 3.11
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Configure poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy application code
COPY . .

# Expose port 3000
EXPOSE 3000

# Run the application with Gunicorn
CMD ["gunicorn", "--threads", "4","--timeout", "4", "--workers", "4" ,"--bind", "0.0.0.0:3000", "app.wsgi:app"]
