#!/bin/bash

# Set the Anthropics API key
export ANTHROPIC_API_KEY="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"

# Set the Smartsheet API key
export SMARTSHEET_API_KEY="93Gjf6pySgOfoLKHhG2PzuJc2YI3Rr0B65mMI"

echo "Environment variables set successfully."

# Generate .env file
cat <<EOF > /Users/kaysonhansen/Desktop/smartsheet-ai-assistant/.env
ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY"
SMARTSHEET_API_KEY="$SMARTSHEET_API_KEY"
EOF

echo ".env file generated successfully."