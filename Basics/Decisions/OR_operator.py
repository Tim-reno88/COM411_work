print("What type of adventure should I have?")
adventure = input()

if (adventure == "short") or (adventure == "scary"):
    print("Entering the dark forest!")
elif(adventure == "long") or (adventure == "safe"):
    print("Entering the safe route!")
else:
    print("Not sure which route to take")
