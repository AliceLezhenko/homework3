#1

class Car:
    def __init__(self,mark,model,year):
        self.mark=mark
        self.model=model
        self.year=year
    def get_info(self):
        print(self.mark,self.model,self.year)

car1=Car("huindai", "accent", 2012)
car1.get_info()



#2

class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def get_salary_info(self):
        print("Заробітна плата "+self.name+" "+str(self.salary))

emp1=Employee("Василій", "тракторист", 13000)
emp1.get_salary_info()