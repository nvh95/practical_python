
import nose
from bubble_sort import bubble_sort
def run(original, expected):
    '''Sort list original and compare it to list expected.'''
    bubble_sort(original)
    assert original == expected

def test_empty():
    '''Test sorting empty list.'''
    run([], [])

def test_one():
    '''Test sorting a list of one value.'''
    run([1], [1])

def test_two_ordered():
    '''Test sorting an already-sorted list of two values.'''
    run([1, 2], [1, 2])

def test_two_reversed():
    '''Test sorting a reverse-ordered list of two values.'''
    run([2, 1], [1, 2])

def test_three_identical():
    '''Test sorting a list of three equal values.'''
    run([3, 3, 3], [3, 3, 3])

def test_three_split():
    '''Test sorting a list with an odd value out.'''
    run([3, 0, 3], [0, 3, 3])

if __name__ == '__main__':
#     a= [1,2,1]
#     bubble_sort(a)
#     print a
    nose.runmodule()