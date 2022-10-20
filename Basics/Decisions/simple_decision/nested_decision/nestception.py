# Ask user for place
print("Where should I look?")
place = input()

# Check the bedroom
if place == "in the bedroom":
    print("Where in the bedroom should I look?")
    bedroom_place = input()

    if bedroom_place == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

# Check the bathroom
elif place == "in the bathroom":
    print("Where in the bathroom should I look?")
    bathroom_place = input()

    if bathroom_place == "in the bath tub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")

# Check the lab
elif place == "in the lab":
    print("Where in the lab should I look?")
    lab_place = input()

    if lab_place == "on the table":
        print("YES! I found my battery")
    else:
        print("Found some tool's but no battery.")
else:
    print("I dont know where that is but I will keep looking")
