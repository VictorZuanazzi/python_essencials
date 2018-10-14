import math

def self_averages(grades):
    '''(list of list of number) -> list of float

    Return a new list in which each item is the average of the grades in the inner list at the corresponding position of grades.

    >>> slef_averages([[70,75,80],[70,80,90,100],[80,100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []
    for i in range(len(grades)):
        averages.append(0)
        for j in range(len(grades[i])):
            averages[i]= averages[i] + grades[i][j]
        averages[i]= averages[i]/len(grades[i])

    return averages

def averages(grades):
    '''(list of list of number) -> list of float

    Return a new list in which each item is the average of the grades in the inner list at the corresponding position of grades.

    >>> averages([[70,75,80],[70,80,90,100],[80,100]])
    [75.0, 85.0, 90.0]
    '''

    class_averages = []
    for grades_list in grades:
        total = 0
        for j in grades_list:
            total = total + j
        class_averages.append(total/len(grades_list))

    return class_averages

def standard_deviation(grades):
    '''(list of list of number) -> list of float

    Return a new list in which each item is the standard deviation of the grades in the inner list at the corresponding position of grades.

    >>> grades = [[70,75,80],[70,80,90,100],[80,100]]
    >>> a= averages(grades)
    >>> a
    [5.0, 15.811388300841896, 10.0]
    '''

    std = []
    mean = averages(grades)
    for i in range(len(grades)):
        total = 0
        for j in grades[i]:
            total = total + pow(j-mean[i],2)
        total = total/(len(grades)-1)

        std.append(pow(total,0.5))
        
    return std












        
