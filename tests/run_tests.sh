#!/bin/bash

# Step 1: Activate virtual environment (Windows)
source venv/Scripts/activate

# Step 2: Run tests
echo "Running test suite..."
pytest tests/

# Step 3: Capture exit code and return 0 (pass) or 1 (fail)
if [ $? -eq 0 ]; then
    echo "✅ All tests passed."
    exit 0
else
    echo "❌ Some tests failed."
    exit 1
fi
