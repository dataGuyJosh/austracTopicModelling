#!/bin/bash

# Specify the directory containing your text files
directory="data"

# Specify the output file where concatenated content will be stored
output_file="output.txt"

# Use find command to locate all text files in the directory and its subdirectories
find "$directory" -type f | while IFS= read -r file; do
    # Use cat command to read the contents of each text file and append them to the output file
    cat "$file" >> "$output_file"
    # Add separation between documents
    echo "|~|~|" >> "$output_file"
done