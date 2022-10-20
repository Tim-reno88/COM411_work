# Ask user what to do
print("What type of cover does the book have hard of soft?")
book_cover = input()

# Decision
if book_cover == "soft":
    print("Is the book_cover perfect bound?")
    perfect_bound = input()

    if perfect_bound == "yes":
        print("Soft cover,Perfect bound books are very popular!")
else:
    print("Books with hard covers can be more expensive!")
