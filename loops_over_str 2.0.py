def collect_vowels(s):
    ''' (str) -> srt

    Return the vowels from s. Do not trat the letter y as a vowel

    >>> collect_vowels ('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels ('xys')
    ''
    '''

    vowels = ''
    for char in s:
        if has_vowel(char):
            vowels = vowels + char

    return vowels


def count_vowels (s):
    '''(str) -> int

    Return the number of vowels in s. Do not treat the letter y as a vowel.

    >>> count_vowels ('Happy anniversary!')
    5
    >>> count_vowels ("xyz")
    0
    '''
    num_vowels = 0
    for char in s:
        if has_vowel(char):
            num_vowels = num_vowels +1
            
    return num_vowels

def has_vowel(s):
    """(str) -> bool

    Return True if and only if s has at least one vowel, not including y.
    
    >>> has_vowel("Anniversary")
    True
    >>> has_vowel("xyz")
    False
    """
    vowel_found = False
    
    for char in s:
        if char in 'aeiouAEIOU':  
           return True

    return vowel_found




