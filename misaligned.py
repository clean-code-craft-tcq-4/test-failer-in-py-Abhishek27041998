
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            s = formatter(i*5 + j, major, minor)
            print(s)
    return len(major_colors) * len(minor_colors)


def formatter(num, major, minor):
    s = f'{num} | {major} | {minor}'
    return s


result = print_color_map()
assert(result == 25)
assert(formatter(10, 'White', 'Orange').find("|") == 2)

print("All is well (maybe!)\n")
