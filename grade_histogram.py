# The program must read a file where ID of students and grades are stored.
# The program must create ranges of grades [0,9]...[90,99],[100]
#and count the number of grades in which range.
# The program must then creat a hitogram of '*' for the ranges and store it in a new file.

def get_id_and_grades():
    '''

    '''
    import file_dialogs
    
    grades_file_path = file_dialogs.open_from()
     #print ('Chose the file with the grades to be analized')

    grades_file = open(grades_file_path, 'r')
    #skips the bullshit
    for i in range(4):
        grades_file.readline()

    id_grade = grades_file.readlines()
    grades_file.close()
    return id_grade

def number_of_grades_in_range(bottom, upside, grades):
    '''
    '''
    number_of_grades = 0
    for i in grades:
        if (i>=bottom) and (i <= upside):    
            number_of_grades = number_of_grades + 1
    return number_of_grades

def save_histogram(number_of_grades, bottom):
    '''(list of int, list of int)-> bool
    '''
    import file_dialogs
    
    histogram_file_path = file_dialogs.save_as()
    histogram_file = open(histogram_file_path, 'w')

    histogram_file.write('That is the distribuition of grades among the students:\n\n')

    title = '[  '+ str(bottom[0]) +' :  ' + str(bottom[0]+9)+' ] '
    stars = '*'*number_of_grades[0]
    histogram_file.write(title + stars + '\n')
    for i in range(1,len(bottom)-1):
        title = '[ '+ str(bottom[i]) +' : ' + str(bottom[i]+9)+' ] '
        stars = '*'*number_of_grades[i]
        histogram_file.write(title + stars + '\n')
    title = '[ '+ str(bottom[-1]) +'     ] '
    stars = '*'*number_of_grades[-1]
    histogram_file.write(title + stars + '\n')

    histogram_file.close()
    return True
    
def grade_histogram():
    '''(str) -> file


    '''
    id_grade = get_id_and_grades()
    
    student_id = []
    student_grade = []
    for i in range(len(id_grade)):
        student_id.append(int(id_grade[i][0:4]))
        student_grade.append(int(id_grade[i][4:]))

    bottom = []
    for i in range(0,101,10):
        bottom.append(i)

    number_of_grades = []
    for i in bottom:
        number_of_grades.append(number_of_grades_in_range(i, i+9, student_grade))

    save_histogram(number_of_grades, bottom)

    

    return True    
    
    
    
