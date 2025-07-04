"""
Given a temperature (in Celsius), print the state of water at that temperature
"""

# Todo: Handle invalid inputs
while True:
    temp = input("What's the H20 temperature? ")
    try:
        temp = float(temp)
        break
    except ValueError as e:
        # diff ways to produce err msg
        print(repr(e))
        print(f"{e!r}")

        print(f"{e}")
        print(f"{e=}")

        print(f"temp {temp} is not a valid number\n")
    except Exception as e:  # capture any other exception
        print(f"e!r" + "\n")


if temp <= 0:
    print("  It’s ice")
elif temp >= 100:
    print("  It’s steam")
else:
    print("  It's water")
