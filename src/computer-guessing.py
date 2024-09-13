# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.


def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


print("Please thing of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

# Here, we implement the computer's strategy for guessing (strategy 1.)
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.
# for guess in range(1, 21):
#     result = input_selection(
#         "I'm guessing {}\nHow is my guess?".format(guess),
#         ["low", "hit", "high"]
#     )
#     if result == "hit":
#         print("Wuhuu!")
#         break

#     print("I must have been too low, right?", result)

# # guessing strategy 2.

# for guess in range(1, 21, -1):
#     result = input_selection(
#         "I'm guessing {}\nHow is my guess?".format(guess),
#         ["low", "hit", "high"]
#     )
#     if result == "hit":
#         print("Wuhuu!")
#         break

#     print("I must have been too high, right?", result)

# guessing strategy 3.

upper, lower = 20, 1
guess = upper // 2
result = ''
while result != 'hit':
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    elif result == 'low':
        lower = guess + 1
    else: 
        upper = guess - 1
    
    guess = (upper + lower) // 2