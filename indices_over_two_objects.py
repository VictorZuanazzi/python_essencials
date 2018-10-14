def sum_items (list1, list2):
    ''' (list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the items at the corresponding position of list1 and list2.

    Precondition: len(list1) == len(list2)

    >>> sum_items([1,2,3],[2,4,2])
    [3,6,5]
    '''

    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])

    return new_list

def count_matches(s1, s2):
    ''' (str, str) -> int

    Return the number of positions in s1 that contain the same character at the corresponding position of s2.

    Precondition: len(s1) == len(2)

    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    '''
    matches = 0
    if (len(s1) == len(s2)):
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                matches = matches +1

    return matches


 
