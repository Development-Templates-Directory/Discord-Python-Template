#!/bin/bash

# Define the source and destination files
ENV_FILE=".env"
EXAMPLE_ENV_FILE=".env.example"

# Check if the .env file exists
if [ ! -f "$ENV_FILE" ]; then
  cat "$EXAMPLE_ENV_FILE" > "$ENV_FILE"
fi

# Create or clear the .env.example file
> "$EXAMPLE_ENV_FILE"

# Extract variable names from .env and write them to .env.example
awk -F= '{ print $1 }' "$ENV_FILE" | grep -v '^#' | while read -r var; do
  echo "$var=" >> "$EXAMPLE_ENV_FILE"
done