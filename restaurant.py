from person import *

ARRIVAL_TIMES = [1, 3, 5, 10, 15, 18, 25, 30, 40, 52, 55, 60, 70, 75, 80, 85, 94, 98]


### START CODE HERE ###
# TODO : Define Restaurant Class
class Restaurant:
    def __init__(self,num_seats, num_employees, closing_time):
        self.num_seats = num_seats #식당에 손님이 앉을 자리 수
        self.closing_time = closing_time #식당의 운영을 마감하는 시각
        self.current_time = 0 #현재 시각
        self.visitors = [] #현재 식당에 자리를 잡고 있는 손님 객체들의 리스트
        self.total_visitors_served = [] #식당에 방문한 손님들 중에서 식당에 서비스를 제공받은 모든 객체들의 리스트
        #self.num_employees = num_employees 
        self.employees = [Employee(i) for i in range(num_employees)] #현재 식당에서 일하고 있는 종업원 객체들의 리스트.
    
    def visitor_arrived(self, visitor_obj):
        #i = len(self.visitors)
        if len(self.visitors) < self.num_seats:
            self.visitors.append(visitor_obj)
            self.total_visitors_served.append(visitor_obj)
       
        else:
            visitor_obj.leave()
    
    def order_process(self):
        for employee in self.employees:
            if employee.state == WAITING:
                for visitor in self.visitors:
                    if visitor.state == ARRIVAL:
                        employee.cook(visitor)
                        break
                else:
                    continue
                break
    def after_one_minute(self):
        leaving_visitors = []  # sate == LEAVING리스트
        #손님 after_one_minute 호출
        for visitor in self.visitors: 
            visitor.after_one_minute(self.current_time)  
            if visitor.state == LEAVING:
                leaving_visitors.append(visitor)
        
        #손님 중 LEAVING state remove
        for visitor in leaving_visitors:
            self.visitors.remove(visitor)
        
        #종업원 after_one_minute 호출
        for employee in self.employees:
            employee.after_one_minute(self.current_time)

    def operate(self):
        while self.current_time < self.closing_time:
            self.current_time += 1
            print(f'Current Time: {self.current_time}')
            if self.current_time in ARRIVAL_TIMES:
                new_visitor = Visitor(self.current_time)
                self.visitor_arrived(new_visitor)
            self.order_process()
            self.after_one_minute()
        self.summarize_result()
    
    def summarize_result(self):
        served_count = len(self.total_visitors_served)
        not_served_count = len(ARRIVAL_TIMES) - served_count
        visitor_wait_times = [v.waiting_time for v in self.total_visitors_served]
        employee_wait_times = [e.waiting_time for e in self.employees]
        employee_work_times = [self.closing_time - e.waiting_time for e in self.employees]

        visitor_avg_wait_time = sum(visitor_wait_times) / served_count if served_count > 0 else 0
        employee_avg_wait_time = sum(employee_wait_times) / len(self.employees)
        employee_avg_work_time = sum(employee_work_times) / len(self.employees)

        print(f"served : {served_count}, not_served : {not_served_count}")
        print(f"visitor average waiting time : {visitor_avg_wait_time:.2f}")
        print(f"employees average waiting time : {employee_avg_wait_time:.2f}")
        print(f"employees average working time : {employee_avg_work_time:.2f}")
### END CODE HERE ###
if __name__ == '__main__':
    rest = Restaurant(5, 2, 100)
    rest.operate()