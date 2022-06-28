
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            num = generate_next_number(i, j)
            s = formatter(num, major, minor)
            print(s)
    return len(major_colors) * len(minor_colors)


def generate_next_number(i, j):  # Separating the function for testing
    return i*5 + j + 1


def formatter(num, major, minor):
    # Formatting the string to print in aligned manner
    s = '{:<5} | {:<10} | {:<10}'.format(num, major, minor)
    return s


result = print_color_map()

# Assert result
assert(result == 25)

# Assert number generation function
assert(generate_next_number(0, 0) == 1)
assert(generate_next_number(4, 4) == 25)
assert(generate_next_number(3, 4) == 20)

# Check if the offset of '|' is common for all formatted lines
assert(formatter(1, 'White', 'Blue').find("|") == 6)
assert(formatter(1, 'White', 'Blue').rfind("|") == 19)

assert(formatter(10, 'Red', 'Slate').find("|") == 6)
assert(formatter(10, 'Red', 'Slate').rfind("|") == 19)

assert(formatter(25, 'Violet', 'Slate').find("|") == 6)
assert(formatter(25, 'Violet', 'Slate').rfind("|") == 19)

print("All is well (maybe!)\n")
