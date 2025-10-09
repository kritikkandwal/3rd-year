class Student:
    
    # default constructor
    def __init__(self):
        pass 

    college_name="lpu" #Class Attr
    
    # Parametrized constructor
    def __init__(self, fullname,marks):
        self.name = fullname #Object Attr
        self.marks=marks
        print("adding new student in Database .. ")

s1 = Student("karan",97)
print(s1.name,s1.marks) #karan

s2 = Student("arjun",99)
print(s2.name,s2.marks)

print(s1.college_name) #the thing is college name is same for all so we make it global
print(s2.college_name)