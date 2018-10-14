import tkinter.filedialog
import clas_grade

al_filename = tkinter.filedialog.askopenfilename()
al_file = open(al_filename, 'r')

al_histfilename = tkinter.filedialog.askopenfilename()
al_histfile = open(al_histfilename, 'w')

# Read the grades into a list.
grades = grade.read_grades(al_file)

# Count the grades per range.
range_counts = grade.count_grade_ranges(grades)


print (range_counts)

# Write the histogram to the file.
grade.write_histogram(range_counts, al_histfile)

al_file.close()
al_histfile.close()

'''
0-9:   *
10-19: **
20-29: ****
  :
90-99: **
100:   *
'''
