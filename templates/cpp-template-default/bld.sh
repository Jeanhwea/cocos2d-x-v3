#!/usr/bin/env bash
set -e

# Check if cmake is installed
if ! command -v cmake &> /dev/null; then
    echo "cmake could not be found"
    exit 1
fi

# Display cmake version
cmake --version

cmake -B build -G"Xcode" --log-level=STATUS

cmake --build build
