# Use Python 3.12.4 as the base image
FROM python:3.12.4-slim

# Set the working directory in the container
WORKDIR /bot

# Copy the current directory contents into the container at /bot
COPY . /bot

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Print debug information and run bot.py
CMD echo "Python version:" && \
    python --version && \
    # Run the bot
    python bot.py