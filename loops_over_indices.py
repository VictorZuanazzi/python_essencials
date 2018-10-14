def count_adjacent_repeats(s):
    '''(str) -> int

    Return the number of occurrences of a character and adjacent charater being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0
    for i in range (len(s)-1):
        if s[i] == s[i+1]:
            repeats = repeats +1
            
    return repeats

def shift_left(L):
    '''(list) -> NoneType

    Shift each item in L one position to the left and shift the first item to the last position.

    Precondition: len(L) >= 1

    >>> shift_left(['a','b','c','d'])
    ['b','c','d','a']
    
    '''

    firstL = L[0]
    for i in range(1,len(L)-1):
        L[i-1] = L[i]
    L[len(L)-1] = firstL
    
