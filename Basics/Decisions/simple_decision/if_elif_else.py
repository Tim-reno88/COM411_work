print("Towards which directions should I paint (Up,down left or right) ?")
direction = input()

# Determine which message to display
if direction == "up":
    print("I am painting in the upwards direction")
elif direction == "down":
    print("I am painting in the downward direction")
elif direction == "left":
    print("I am painting in the left direction")
elif direction == "right":
    print("I am painting in the right direction")
else:
    print("I am not painting")
