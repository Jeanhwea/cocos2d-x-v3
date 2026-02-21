#!/usr/bin/env bash

cmake -B build -G"Xcode" --log-level=STATUS

cmake --build build
