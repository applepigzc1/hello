class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name + 'is siting')
        
    def stand(self):
        print(self.name + int(self.age) + 'is standing')
        
    def update_age(self,age):
        self.age = age
    
    def add_arg(self,arg):
        self.arg = arg
        print(self.arg)
        
    
class One_Dog(Dog):
    pass
