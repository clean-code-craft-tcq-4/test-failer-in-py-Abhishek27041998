from tshirts import size


def test_sizes():
    assert(size(37) == 'S')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    assert(size(38) == 'M')
    assert(size(42) == 'L')

    print("All is well (maybe!)\n")
