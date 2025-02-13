#!/bin/bash

# Ensure the script exits on errors and undefined variables
set -euo pipefail

# Add -x for debugging:  Print each command before execution.
set -x

# Define paths and variables
OUTPUT_DIR="$PWD/team_chat/"

# Source the .env file if it exists
if [[ -f .env ]]; then
    source .env
fi

# Check if DISCORD_TOKEN is set
if [[ -z "${DISCORD_TOKEN:-}" ]]; then
    echo "Error: DISCORD_TOKEN not found in .env file"
    exit 1
fi

# Prompt for channel ID
read -r -p "Enter the Discord channel ID: " CHANNEL_ID
if [[ -z "$CHANNEL_ID" ]]; then
    echo "Error: Channel ID cannot be empty"
    exit 1
fi

# Check if Docker is installed and running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not installed or not running."
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"
if [[ $? -ne 0 ]]; then
    echo "Error: Failed to create output directory: $OUTPUT_DIR"
    exit 1
fi

# Run the Docker command to export the Discord channel
docker run --rm -i \
    -v "$OUTPUT_DIR:/out" \
    --env DISCORD_TOKEN="$DISCORD_TOKEN" \
    tyrrrz/discordchatexporter:stable export \
    -f "Json" \
    -c "$CHANNEL_ID" \
    -t "$DISCORD_TOKEN"

# checking return code from docker
if [[ $? -ne 0 ]]; then
    echo "Error: Docker command failed."
    exit 1
fi

echo "Export complete. Files saved to $OUTPUT_DIR"

# Run the Python script to compress the conversation
python3 compress_conversation.py "$CHANNEL_ID"
