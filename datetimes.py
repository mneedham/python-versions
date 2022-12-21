from datetime import datetime as dt

datetime_strings = [
    '2011-11-04', '20111104',
    '2011-11-04 00:05:23', '2011-11-04T00:05:23Z',
    '2011-11-04T00:05:23+04:00', '2022-095'
]

def parsing_decorator(fn, value):
    print(f"➡️\t{value}")
    try:
        print(f"✅\t{fn(value)}")
    except ValueError as err:
        print(f"❌\t{err}")

for value in datetime_strings:
    parsing_decorator(dt.fromisoformat, value)
    print()