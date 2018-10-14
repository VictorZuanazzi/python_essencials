def save_as():
    '''() -> str

    Returns the path to the file to be writen in another program.
    
    '''

    import tkinter.filedialog

    return tkinter.filedialog.asksaveasfilename()
    
    
def open_from():
    '''() -> str

    Returns the path to the file to be read in another program.
    '''

    import tkinter.filedialog

    return tkinter.filedialog.askopenfilename()
    
