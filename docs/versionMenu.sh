#!/bin/bash

# Get tags from the current repository
repo_path="../"
cd $repo_path
tags=$(git tag | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' | sort -V | awk '$0 > "v0.1.0"')

# Remove the last tag
tags=$(echo "$tags" | head -n -1)

# Read the current content of index.rst
index_file="docs/index.rst"
lines=$(cat $index_file)

# Find the line number where "Documentation Version" starts
start_line=$(grep -n "Documentation Version" $index_file | cut -d: -f1 | head -n 1)

# Keep content before "Documentation Version"
if [ -n "$start_line" ]; then
    lines=$(head -n $(($start_line - 1)) $index_file)
fi

# Create the rst content
rst_content="Documentation Version\n"
rst_content+="====================\n\n"

for version in $tags; do
    rst_content+="    * \`$version <https://ionutmuthi.github.io/docVersionTest/$version/index.html>\`__\n"
done

# Append the new content
lines+="$rst_content"

# Write the updated content back to index.rst
echo -e "$lines" > $index_file
