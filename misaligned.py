
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            s = formatter(i*5 + j, major, minor)
            print(s)
    return len(major_colors) * len(minor_colors)


def formatter(num, major, minor):
    s = "{:<3}| {:<10}| {:<10}".format(str(num), major, minor)
    return s


result = print_color_map()
assert(result == 25)
assert(formatter(1, 'White', 'Orange').find("|") == 3)
print("All is well (maybe!)\n")
