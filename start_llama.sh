#!/bin/bash

# Load model value from config.yaml
MODEL=$(grep 'model:' config.yaml | awk '{print $2}')

# Kill any existing Ollama processes
echo "Checking for any existing Ollama processes..."
pkill -f "ollama" && echo "Terminated existing Ollama processes." || echo "No existing Ollama processes found."

# Wait briefly to ensure processes are fully terminated
sleep 2

# Start Ollama as a background service, redirecting logs to a file
echo "Starting Ollama service..."
nohup ollama run "$MODEL" > /tmp/ollama_start.log 2>&1 &

# Wait a moment to allow the service to initialize
sleep 3

# Check if the Ollama service started successfully
if pgrep -f "ollama" > /dev/null; then
    echo "Ollama service started successfully."
else
    echo "Failed to start Ollama service. Check /tmp/ollama_start.log for details."
fi