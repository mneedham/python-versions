import platform
import json

print(
    json.dumps({
        "Version": platform.python_version()
    })
)