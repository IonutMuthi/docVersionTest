import json

# Read the tags.json file
with open('tags.json', 'r') as file:
    data = json.load(file)

# Extract versions
versions = data.get('versions', [])

# Create the rst content
rst_content = "Documentation Version\n"
rst_content += "=" * len(rst_content) + "\n\n"
rst_content += ".. toctree::\n\n"

for version in versions:
    rst_content += f"    * `{version} <https://ionutmuthi.github.io/docVersionTest/{version}/index.html>`__\n"

# Save the content to versionMenu.rst
with open('versionMenu.rst', 'w') as file:
    file.write(rst_content)