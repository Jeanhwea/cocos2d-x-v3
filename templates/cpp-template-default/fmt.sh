#!/usr/bin/env bash
set -e

# Check if clang-format is installed
if ! command -v clang-format &> /dev/null; then
    echo "clang-format could not be found"
    exit 1
fi

for src_file in $(find $PWD/Classes -iname "*.cpp" -or -iname "*.h"); do
    echo "Format $src_file"
    clang-format -i $src_file
done
