# def is_positive(number):
#     if number < 0:
#         return f"{number} is a negative number."
#     return f"{number} is a positive number."

def is_positive(number):
    if number < 0:
        return f"{number} is a negative number."
    elif number > 0:
        return f"{number} is a positive number."
    else:
        return "It is zero."
# Here you make manual testing through testing with the argument
print(is_positive(0))
