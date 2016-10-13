import nose
from prefixes import all_prefixes
def test_length_of_4():
    assert all_prefixes('hung') == set(['h', 'hu','hun','hung'])
    
def test_length_of_1():
    assert all_prefixes('h') == set(['h'])

if __name__ == "__main__":
    nose.runmodule()