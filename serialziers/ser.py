class Person:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def show(self):
        return f'My name is {self.fname} {self.lname}, and I am {self.age} years old.'
    
    
    