def read_grades(gradefile):
    '''(file open for reading) -> list of float

    Read and return the list of grades in the gradefile.

    Precondition: gradefile starts witha a header that contains no blank lines,
    then has a blank line, then lines containing a student number and grade.
    '''

    # Skip over the header.

    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
 
    # Read the grades, accumulating them into a list.

    grades = []
    
    line = gradefile.readline()
    while line != '':
        #Now we have a string containing the info for a single student.
        #Find the last space and take everything after that space.
        grade = line[line.rfind(' ')+1:]
        grades.append(float(grade))
        line = gradefile.readline()

    return grades

def count_grade_ranges(grades):
    '''(list of float) - list of int

    Return a list of int where each index indicates how many grades were in there ranges:


    0-9:   *
    10-19: **
    20-29: ****
      :
    90-99: **
    100:   *

    >>> count_grade_ranges([78.0, 9.2, 45.3, 96.3, 63.1, 14.2, 85.5, 24.9, 33.3, 6.5, 99.9 ,9.0])
    [2, 1, 1, 1, 1, 0, 1, 1, 1, 2, 0]
    '''
    range_counts = [0]*11

    for grade in grades:
        which_range = int(grade//10)
        range_counts[which_range] = range_counts[which_range] +1

    return range_counts

def write_histogram (range_counts,histfile):
    '''(list of int, file open for writing) -> NOteType

    Write a histogram of *'s based on the number of grades in each range.
    The output format:
    0-9:   *
    10-19: **
    20-29: ****
      :
    90-99: **
    100:   *
    '''
    histfile.write('0-9:   ')
    histfile.write('*'*range_counts[0]+'\n')

    #Write the 2-digit ranges.
    for i in range (1,10):
        low= i*10
        high = i*10+9
        histfile.write(str(low)+ '-'+str(high)+': ')
        histfile.write('*'*range_counts[i]+'\n')
                       
    histfile.write('100:   ')
    histfile.write('*'*range_counts[-1]+'\n')
    
    










    
