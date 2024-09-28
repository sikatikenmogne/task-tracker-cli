FROM mcr.microsoft.com/devcontainers/python:3.10

# Set the working directory in the container
WORKDIR /app

# Install Poetry, Pipx, and Bash
RUN apt-get update && apt-get install -y bash \
    && pip install poetry pipx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pipx ensurepath

# Configure Poetry to not create a virtual environment
RUN poetry config virtualenvs.create false

# Copy the source code into the container
COPY . .

# Ensure README.md exists to avoid metadata generation issues
RUN if [ ! -f README.md ]; then echo "# Task Tracker CLI" > README.md; fi

# Copy the pyproject.toml and poetry.lock files to the container
# COPY pyproject.toml poetry.lock ./

# Install the dependencies using Poetry
RUN poetry install

# Install the CLI application using Pipx
RUN pipx install . --force

# Create a non-privileged user
# RUN useradd -m appuser

# Ensure the data.json file has the correct permissions
# RUN touch data.json && chown appuser:appuser data.json

# Switch to the non-privileged user to run the application
# USER appuser

# Set the entry point for the CLI application
ENTRYPOINT ["task-cli"]
