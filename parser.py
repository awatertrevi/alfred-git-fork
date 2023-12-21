import json
import sys
import os
import re

# read file
filePath = os.path.join(os.path.expanduser(
    '~'), 'Library/Application Support/com.DanPristupov.Fork/repositories.json')

with open(filePath, 'r') as file:
    data = file.read()

# parse file
repositories = json.loads(data)['repositories']

# sort
repositories = sorted(repositories, key=lambda k: k['name'])
items = []
for repository in repositories:
    item = {
        "title": repository['name'],
        "arg": repository['path']
    }
    if sys.argv[1]:
        if sys.argv[1].lower() in repository['name'].lower():
            items.append(item)
    else:
        items.append(item)

result = {
    "items": items
}

output = json.dumps(result)
print(output)

sys.exit(0)
