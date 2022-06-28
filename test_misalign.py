def test_misalignment():
    from misaligned import print_color_map, generate_next_number, formatter
    result = print_color_map()

    # Assert result
    assert (result == 25)

    # Assert number generation function
    assert (generate_next_number(0, 0) == 1)
    assert (generate_next_number(4, 4) == 25)
    assert (generate_next_number(3, 4) == 20)

    # Check if the offset of '|' is common for all formatted lines
    assert (formatter(1, 'White', 'Blue').find("|") == 6)
    assert (formatter(1, 'White', 'Blue').rfind("|") == 19)

    assert (formatter(10, 'Red', 'Slate').find("|") == 6)
    assert (formatter(10, 'Red', 'Slate').rfind("|") == 19)

    assert (formatter(25, 'Violet', 'Slate').find("|") == 6)
    assert (formatter(25, 'Violet', 'Slate').rfind("|") == 19)

    print("All is well (maybe!)\n")