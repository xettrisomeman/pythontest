import file2



def test_add():
    assert file2.add(7,3) == 10
    assert file2.add(7) == 9
    assert file2.add(5) == 7


def test_product():
    assert file2.product(5,5) == 25
    assert file2.product(5) == 10

    


