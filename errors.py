import traceback

# Divide by zero
x,y,z = (4,6,0)
try:
    result = x / y  / z
    print(result)
except Exception:
    print(traceback.format_exc())

# Missing key
person1 = {
    "person": {
        "name": "Mark",
        "address": {
            "street": "London Road"
        }
    }
}

try:
    postcode = person1["person"]["address"]["postcode"]
    print(postcode)
except Exception:
    print(traceback.format_exc())

# None values
person2 = None
try:
    postcode = person2["person"]["address"]["postcode"]
    print(postcode)
except Exception:
    print(traceback.format_exc())
