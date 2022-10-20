print("what level of brightness is required?")
brightness = int(input())

print("\nAdjusting brightness...\n")

for brightness in range(2, brightness + 1, 2):
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Bop's brightness level: {'*' * brightness}")

print("Adjustments complete!")