import platform
print(f"Version: {platform.python_version()}")

# Missing key
person1 = {
    "person": {
        "name": "Mark",
        "address": {
            "street": "London Road"
        }
    }
}

postcode = person1["person"]["address"]["postcode"]
print(postcode)
