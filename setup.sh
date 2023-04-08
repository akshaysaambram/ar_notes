#!/bin/bash

# Install pip if not installed
if ! command -v pip &> /dev/null
then
    echo "pip not found. Installing pip..."
    sudo apt-get update
    sudo apt-get -y install python3-pip
fi

# Create new virtual environment
python3 -m venv djangoenv

# Activate virtual environment
source djangoenv/bin/activate

# Clone the GitHub repository
git clone https://github.com/akshaysaambram/ar_notes.git

# Install dependencies
pip install -r ar_notes/requirements.txt

# Check if all dependencies are installed
missing_deps=()
for dep in $(cat requirements.txt); do
    if ! pip show $dep &> /dev/null
    then
        missing_deps+=($dep)
    fi
done

# Output missing dependencies
if [ ${#missing_deps[@]} -eq 0 ]; then
    echo "All dependencies installed."
else
    echo "The following dependencies are not installed:"
    printf '%s\n' "${missing_deps[@]}"
fi
