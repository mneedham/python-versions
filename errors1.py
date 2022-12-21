import platform
print(f"Version: {platform.python_version()}")

# Divide by zero
x,y,z = (4,6,0)
result = x / y  / z
print(result)
