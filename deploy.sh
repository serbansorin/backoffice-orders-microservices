#!/bin/bash

# Loop through all directories
for dir in */ ; do
  # Go into directory
  cd "$dir"

  # Run npm commands
  echo "Running npm install and build in $dir"
  npm install
  npm run build

  # Go back to root directory
  cd ..

done