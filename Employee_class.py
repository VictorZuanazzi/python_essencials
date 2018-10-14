class Employee(object):

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last + '@company.com'


    def fullname(self):
        return self.first + ' ' + self.last

    

        
        

