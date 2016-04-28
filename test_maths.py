import cal


def test_square():
    x = 4
    assert cal.square(x) == 16

def test_cube():
    x = 4
    assert cal.cube(x) == 64

def test_add():
    assert cal.add(3,4) == 7

