FROM python:3.13
# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*
# Download and install Ollama binary directly
# Download and install Ollama binary directly

RUN curl -L -o /usr/local/bin/ollama https://github.com/ollama/ollama/releases/download/v0.1.32/ollama-linux-amd64 && \
    chmod +x /usr/local/bin/ollama

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
RUN ls -la /app  # Check if all files are there
RUN ls -la /app/templates  # Check if templates exist
RUN ls -la /app/static  # Check if static files exist


EXPOSE 8080

# Create ollama directory
RUN mkdir -p /root/.ollama

# Create a startup script that pulls the model and runs both services
# Create a startup script that runs the model and then starts Python
RUN echo '#!/bin/bash\n\
# Start Ollama in background\n\
ollama serve &\n\
\n\
# Wait for Ollama to start\n\
sleep 10\n\
\n\
# Pull the model first\n\
echo "Pulling llama3:8b model..."\n\
ollama pull llama3:8b\n\
\n\
# Run the model (this will keep it loaded in memory)\n\
echo "Running llama3:8b model..."\n\
ollama run llama3:8b &\n\
\n\
# Wait a bit for the model to load\n\
sleep 15\n\
\n\
# Start your Python application\n\
echo "Starting Python application..."\n\
python main.py' > start.sh && chmod +x start.sh

# Run the startup script
CMD ["./start.sh"]




