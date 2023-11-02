ARRIVAL = 'arrival'
WAITING = 'waiting'
EATING = 'eating'
WORKING = 'working'
LEAVING = 'leaving'


### START CODE HERE ###
# TODO 1 : Define Person Class
class Person:
    def __init__(self,person_id):
        self.person_id = person_id
        self.waiting_time = 0
        self.state = None
        
# TODO 2 : Define Visitor Class
class Visitor(Person):
    def __init__(self, arrival_time):
        super().__init__(arrival_time)
        self.waiting_time = 0
        self.state = ARRIVAL 
        self.remaining_eating_time = 0 
        
    def order(self):
        self.state = WAITING 
        
    def eat(self):
        self.state = EATING  
        self.remaining_eating_time = 20  
        
    def leave(self):
        self.state = LEAVING 
        
    def after_one_minute(self, curr_time):
        if self.state == EATING:
            if self.remaining_eating_time > 0:
                self.remaining_eating_time -= 1
            else:
                    self.leave() 
        elif self.state == ARRIVAL:
            self.waiting_time += 1
        elif self.state == WAITING:
            self.waiting_time += 1      
        print(self)
    
    def __str__(self):
        return f"visitor arrived at {self.person_id},{self.state}" 

# TODO 3 : Define Employee Class
class Employee(Person):
    def __init__(self, person_id):
        super().__init__(person_id)
        self.waiting_time = 0
        self.state = WAITING
        self.remaining_cooking_time = 0
        self.visitor = None 
    def cook(self, visitor):
        visitor.order()
        self.state = WORKING
        self.remaining_cooking_time = 15
        self.visitor = visitor
    def serve(self):
        self.visitor.eat()
        self.state = WAITING
        self.visitor = None
    def after_one_minute(self,curr_time):
        if self.state == WORKING:
            if self.remaining_cooking_time > 0:
                self.remaining_cooking_time -= 1
            else:
                self.serve()
        else:
            self.waiting_time += 1
        print(self)
    def __str__(self):
        return f"employee id {self.person_id}, {self.state}"
### END CODE HERE ###
