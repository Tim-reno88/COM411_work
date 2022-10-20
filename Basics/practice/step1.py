# Question for user
print("where would you like to go?")
location = input()

# First option
if location == "shop":
    print("will you walk?")
    option = input()
    if option == "yes":
        print("It is good exercise")
    else:
        print("rather lazy")
# Second option
elif location == "park" or "garden":
    print("It is a good day for it")
# Third option
else:
    print("fuck off")