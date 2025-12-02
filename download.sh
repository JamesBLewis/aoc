#!/bin/bash

# Usage: ./download.sh <year> <day>
YEAR=$1
DAY=$2

# Session cookie from environment variable
SESSION_COOKIE="$SESSION_COOKIE"

# Base path
BASE_PATH="/Users/jameslewis/PycharmProjects/aoc"

# Create directories if they don't exist
mkdir -p "$BASE_PATH/$YEAR/$DAY"

# Download the real input
curl -b "session=$SESSION_COOKIE" "https://adventofcode.com/$YEAR/day/$DAY/input" -o "$BASE_PATH/$YEAR/$DAY/input"

echo "Downloaded input to '$BASE_PATH/$YEAR/$DAY/input'"
