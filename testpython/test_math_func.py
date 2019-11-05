from math_func import StudentDB
import pytest 



@pytest.fixture
def db():
    print("=======SETUP=======")
    db = StudentDB()
    db.connect("data.json")
    return db


def test_martin_data(db):
    martin_data = db.get_data('Martin')
    assert martin_data['id'] == 1
    assert martin_data['name'] == 'Martin'
    assert martin_data['age'] == 18


def test_joaquin_data(db):
    martin_data = db.get_data('Joaquin')
    assert martin_data['id'] == 2
    assert martin_data['name'] == 'Joaquin'
    assert martin_data['age'] == 40

