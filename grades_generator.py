# This program generates random grades with a certain distribution.

def generate_id(number_of_ids):
    '''(int)->list of int

    Return a list of random generated ids of size number_of_ids.
    No ID is generated twice, up to 4000 ids can be generated.
    IDs alway have 4 digits.

    >>> generate_id(4)
    [5000, 5002, 4999, 5003]

    >>> generate_id(-4)
    'We have a problem, \nit is only possible to generate a positive number of IDs'
    '-4 is <= 0'
    []

    '''
    import random
    
    #check for number_of_ids bellow or above the allowed range [1:4000].
    if number_of_ids <= 0:
        print('We have a problem, \nit is only possible to generate a positive number of IDs')
        print(str(number_of_ids) + ' is <= 0')
        return []
    elif number_of_ids > 4000:
        print('We have a problem, \nit is only possible to generate up to 4000 ids')
        print(str(number_of_ids) + ' is > 4000')
        print('4000 ids will be generated')
        return generate_id(4000)
    else:
        # simple formula to generate random id numbers that will not repeat nor be in sequence.
        student_id = []
        student_id.append(random.randint(4001,5999))
        i = 1
        while i < number_of_ids:
            new_id = student_id[0]+ pow(-1,i)*random.randint(i,i+1)
            student_id.append(new_id)
            i = i +1
        return student_id

def generate_grade(number_of_grades):
    '''(int)->list of int

    Return a list of random generated grades of size number_of_grades.
    No id is generated twice.

    >>> generate_grade(4)
    [75, 82, 90, 15]
    
    >>> generate_id(-4)
    'We have a problem, \nit is only possible to generate a positive number of grades'
    '-4 is <= 0'
    []

    '''
    import random
    
    #check for number_of_grades is bellow or above the allowed range [1:4000].
    if number_of_grades <= 0:
        print('We have a problem, \nit is only possible to generate a positive number of grades')
        print(str(number_of_grades) + ' is <= 0')
        return []
    elif number_of_grades > 4000:
        print('We have a problem, \nit is only possible to generate up to 4000 grades')
        print(str(number_of_grades) + ' is > 4000')
        print('4000 ids will be generated')
        return generate_grade(4000)
    else:
        student_grade = []
        i = 0
        while i < number_of_grades:
            # silly formula to generate random grades that are not too uniformelly distributed
            #new_grade = pow(random.randint(random.randint(0,8),10), 2) + pow(-1,i)*random.randint(-5,5) 
            #new_grade = 100 - pow(random.randint(0,10), 2) + pow(-1,i)*random.randint(-5,5)
            new_grade = 64 - pow(random.randint(0,8), 2) + pow(random.randint(0,6), 2)
            student_grade.append(new_grade)
            i = i +1
        return student_grade
    

def grades_generator(number_of_students):
    import random
    import file_dialogs

    Line1 = '* Assignment 1, grades:\n'
    Line2 = '* Colums:\n'
    Line3 = '* id  grade\n'
    Line4 = '\n'

    file_path = file_dialogs.save_as()
    file_grades = open(file_path, 'w')

    file_grades.write(Line1+Line2+Line3+Line4)
    
    student_id = generate_id(number_of_students)
    student_grade = generate_grade(number_of_students)

    id_grade = ''
    for i in range(number_of_students):
        id_grade = id_grade + str(student_id[i]) + ' ' + str(student_grade[i]) + '\n'
        
    file_grades.write(id_grade)   

    file_grades.close()
    return True
    
