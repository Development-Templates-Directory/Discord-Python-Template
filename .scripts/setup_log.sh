#!/bin/bash

# Define the logs directory
LOGS_DIR="./logs"

# Check if the logs directory exists
if [ -d "$LOGS_DIR" ]; then
    # Remove all contents of the directory (but keep the directory itself)
    rm -rf "$LOGS_DIR"/*
else
    # Create the logs directory
    mkdir -p "$LOGS_DIR"
fi
