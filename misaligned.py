
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
    return i*5 + j


def formatter(num, major, minor):
    s = f'{num} | {major} | {minor}'
    return s


result = print_color_map()
assert(result == 25)
assert(formatter(10, 'White', 'Orange').find("|") == 2)
assert(generate_next_number(0, 0) == 1)  # First number is 1 but this implementation returns 0
print("All is well (maybe!)\n")
