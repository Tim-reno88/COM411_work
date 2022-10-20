with open("txt demo") as file:
    for line in file:
        print(line, end="")


print("\n-----Changing the file-----")
new_content = "this is a brand new line\nand another"
with open("txt demo", "w") as file:
    file.write(new_content)
