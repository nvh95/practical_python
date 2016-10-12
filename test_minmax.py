import nose
from minmax import find_two_smallest
def test_maxmin():
    '''Test if finding max and min index is correct'''
    assert find_two_smallest([1,2]) ==(0,1) , 'Fails short lists'
    assert find_two_smallest([7,2,3,4,4,5,]) == (1,2), "Fails long lists"

if __name__ == '__main__': 
    print 1
    print find_two_smallest([1,2]) ==(1,2)
    print 10
    nose.runmodule()
    