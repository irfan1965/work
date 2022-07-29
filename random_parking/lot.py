
class Vehicle:
    def __init__(self,Name,Number):
        self.Name=Name
        self.Number=Number
class bike(Vehicle):
    def __init__(self,Name,Number):
        Vehicle.__init__(self,Name,Number)
class car(Vehicle):
    def __init__(self,Name,Number):
        Vehicle.__init__(self,Name,Number)
class bus(Vehicle):
    def __init__(self,Name,Number):
        Vehicle.__init__(self,Name,Number)