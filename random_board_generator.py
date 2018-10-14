import random
import tkinter.filedialog
"""
v 1.0
Patrick M. Dennis, MD
May 10, 2017
Generates a random n x n board of letters preserving English frequency
"""

def word_frequency_list():
    """
    (specific table* of English word frequency) ->
    Ordered list, freq_list, of 2-value lists, first valoe is specific character, 'A' - 'Z',
    second is float of cumulative frequency (0 - 100) calcuated from frequency lists.
     * The input is a comma separated text file generated from this table:
    https://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    """
    try:
        freq_file = open('Cornell_Letter_Frequency.txt', 'r')
    except FileNotFoundError:
        print("file, 'Cornell_Letter_Frequency.txt' not found ")
        exit(1)
    freq_lst = []
    for line in freq_file:
        spl = line.strip().split(',')
        spl_lst = [spl[3], float(spl[4])]
        freq_lst.append(spl_lst)
    freq_file.close()
    freq_lst.sort(key=lambda x: x[1])
    sum = 0
    for item in freq_lst:
        sum = sum + item[1]
        item[1] = sum
    return(freq_lst)

def build_board(num_rows, num_columns, frequency_list):
    """
    (int, int, list of lists) ->  n x n matrix of Enclish letters in a weighted random distribution
    approximately in accordance with their frequency in English.
    In addition to num_rows and num_columns, takes as input frequency_list, an ordered list of 2-value lists,
    first valoe is specific character, 'A' - 'Z', second is float of cumulative frequency (0 - 100).
    """
    board_lst = []
    for x in range(num_rows):
        new_row = []
        for y in range(num_cols):
            rnd = random.random() * 100
            for item in frequency_list:
                if item[1] > rnd:
                    char = item[0]
                    # if char in 'ETAOIN':
                    #     rel = rel + 1
                    break
            new_row.append(char)
        board_lst.append(new_row)

    out_file = tkinter.filedialog.asksaveasfilename()
    output = open(out_file, 'w')
    for item in board_lst:
        for ch in item:
            output.write(ch)
        output.write('\n')
    output.close()

if __name__ == '__main__':
    num_rows = 100
    num_cols = 100
    build_board(num_rows, num_cols, word_frequency_list())

