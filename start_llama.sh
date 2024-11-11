#!/bin/bash

# Define the absolute path to the config.yaml file
CONFIG_FILE="$(dirname "$0")/config.yaml"

# Load model value from config.yaml
MODEL=$(grep 'model:' "$CONFIG_FILE" | awk '{print $2}')

# Kill any existing Ollama processes
echo "Checking for any existing Ollama processes..."
pkill -f "ollama" && echo "Terminated existing Ollama processes." || echo "No existing Ollama processes found."

# Wait briefly to ensure processes are fully terminated
sleep 2

# Start Ollama as a background service, redirecting logs to a file
echo "Starting Ollama service..."
nohup ollama run "$MODEL" > /tmp/ollama_start.log 2>&1 &

# Retry loop to wait for the Ollama service to start
max_retries=5
retry_interval=5
attempt=1

echo "Waiting for Ollama service to be available..."

while ! pgrep -f "ollama" > /dev/null; do
    if [ "$attempt" -gt "$max_retries" ]; then
        echo "Failed to start Ollama service after $max_retries attempts."
        echo "Check /tmp/ollama_start.log for details."
        exit 1
    fi

    echo "Attempt $attempt: Ollama not yet available, retrying in $retry_interval seconds..."
    sleep "$retry_interval"
    ((attempt++))
done

echo "Ollama service started successfully and is now accessible."
