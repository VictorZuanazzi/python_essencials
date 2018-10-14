def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence dna is valid.
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G').
    A string is not a valid DNA sequence if it contains lowercase letters.
    
    >>>is_valid_sequence('ATCG')
    True
    >>>is_valid_sequence('AtCG')
    False
    >>>is_valid_sequence('ATCPG')
    False
    >>>is_valid_sequence('ATC8G')
    False
    >>>is_valid_sequence('AT!CG')
    False
    >>>is_valid_sequence('AT')
    True
    '''
    valid = True
    
    for char in dna:
        if not char in 'ATCG':
            valid = False
            return valid

    return valid


def insert_sequence(dna1, dna2, position):
    ''' (str, str, int) -> str

    
    Return the DNA sequence obtained by inserting the second DNA sequence dna2 into the first DNA sequence nda1 at the given index position.
    
    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>>insert_sequence('CCGG', 'AT', -2)
    'CCATGG'
    >>>insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    '''
    final_dna = dna1[0:position] + dna2 + dna1[position:]

    return final_dna

def get_complement(nucleotide):
    ''' (str) -> str

    Return the nucleotide's complement.
    T and A always complement each other, C and G always complement each other.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    '''
    dna = 'ATCG'
    complement_dna = 'TAGC'
    if is_valid_sequence(nucleotide):
        return complement_dna[dna.find(nucleotide)]
    else:
        return '-'

def get_complementary_sequence(dna_sequence):
    ''' (str)-> str

    Return the DNA sequence that is complementary to the given nda_sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('ATCG')
    TAGC'

    '''
    
    complement_dna = ''
    for char in dna_sequence:
        complement_dna = complement_dna + get_complement(char)

    return complement_dna
    
        
        
































    
