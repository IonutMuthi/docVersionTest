import subprocess
import re

def get_git_tags(repo_path):
    result = subprocess.run(['git', 'tag'], cwd=repo_path, stdout=subprocess.PIPE, text=True)
    tags = result.stdout.splitlines()
    pattern = r'v\d+\.\d+\.\d+'
    regex = re.compile(pattern)
    filtered_tags = [tag for tag in tags if regex.match(tag)]
    return filtered_tags

# Get tags from the current repository
repo_path = '../'
tags = get_git_tags(repo_path)

# Read the current content of index.rst
with open('index.rst', 'r') as file:
    lines = file.readlines()

# Find the line number where "Documentation Version" starts
start_line = None
for i, line in enumerate(lines):
    if "Documentation Version" in line:
        start_line = i
        break

# Keep content before "Documentation Version"
if start_line is not None:
    lines = lines[:start_line]

# Create the rst content
rst_content = "Documentation Version\n"
rst_content += "=" * len("Documentation Version") + "\n\n"

for version in tags:
    rst_content += f"    * `{version} <https://ionutmuthi.github.io/docVersionTest/{version}/index.html>`__\n"

# Append the new content
lines.append(rst_content)

# Write the updated content back to index.rst
with open('index.rst', 'w') as file:
    file.writelines(lines)