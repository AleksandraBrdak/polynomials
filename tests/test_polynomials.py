from polynomials import Polynomial


def test_print():

    f = Polynomial((1, 0, 0, 0))

    assert str(f) == "1"