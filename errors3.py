import platform
print(f"Version: {platform.python_version()}")

person2 = {"person": None}
postcode = person2["person"]["address"]["postcode"]
print(postcode)
