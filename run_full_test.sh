#!/bin/bash
set -e

# Run the agent
echo "Running agent..."
python test.py

# Format the conversation log to BDD .feature file
echo "Formatting conversation log to BDD .feature file..."
python Result/bdd_formatter.py

# Kill all chromium and playwright processes
pkill -f chromium
pkill -f playwright

# Copy the latest .feature file to features/
echo "Copying .feature file to features/ directory..."
LATEST_FEATURE=$(ls -t Result/bdd_result_*.feature | head -n1)
cp "$LATEST_FEATURE" features/

# Run Behave to generate HTML report
echo "Running Behave to generate HTML report..."
behave -f behave_html_formatter:HTMLFormatter -o Result/report.html


echo "Done! Open Result/report.html in your browser to view the report." 