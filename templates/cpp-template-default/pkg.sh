#!/usr/bin/env bash

# Check if cmake is installed
if ! command -v cmake &> /dev/null
then
    echo "cmake could not be found"
    exit
fi

# Display cmake version
cmake --version

cmake -B output -G"Xcode" --log-level=STATUS

cmake --build output --config Release

mkdir -p dist
mv output/bin/cc04-physics-engine/Release/cc04-physics-engine.app dist
