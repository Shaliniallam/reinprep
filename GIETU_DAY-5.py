#qts 1:
'''wecare insurance company wants to calculate premium of vechicles.
--->vechicles are of 2 types:"two wheelr" and "four wheeler" each vechicle is identified by vechicle id,type,cost and premium cost.
--->vechicles are of 2 % of 2 wheeler vechicle and 6% for four wheeler vechicle
calculate the premium amount and display the vechicle details
write a python prgm to implement the class choosen with its attribute and methods
note:consider all instances variables to be private and methods to be public .
Include getter and setter methods for all instance variables and display appropriate error msgs,if the vechicle type is'''


#insurance company #premium cost of vechicle

'''class Fun():
    def func(self,vehicle_id,type,cost,pre_amount):
        self.vehicle=vehicle_id
        self.type=type
        self.cost=cost
        self.pre_amount=pre_amount

    def get_func(self):
        if(self.type=="two wheelers"):
            pre_amount=(2/100)*self.cost
            
        elif(self.type=="Four wheelers"):
            pre_amount=(6/100)*self.cost
        return pre_amount    
            
  
F1=Fun()
F1.func(50,"two wheelers",100,0)
print(F1.get_func())'''



'''class Fun():
    def __init__(self,vehicle_id,type1,cost,pre_amount):
        self.__vehicle_id=vehicle_id
        self.__type1=type1
        self.__cost=cost
        self.__pre_amount=pre_amount

    def get_func(self):
        if(self.__type1=="Two wheelers"):
            pre_amount=(2/100)*self.__cost
            
        elif(self.__type1=="Four wheelers"):
            pre_amount=(6/100)*self.__cost
        else:
            pre_amount="error"
        return pre_amount
    def set_func(self):
        print(self.__pre_amount)
    def display(self):
        print("the vehicle details are",self.__type1)
 
F1=Fun(500,"Four wheelers",100,0)
print(F1.get_func())
F1.display() '''





#qts-->2:
'''#A university wants to automate their addmission process.
students are admitted based on marks scored in a qualifying exam.
 A student is identified by student id,age,marks in qualifying exam
data are valid,if :
        # age is greater than 20
          marks is between 0 to 100(both inclusive)
          A student qualifies for admission,if
          age and marks are valid and marks is 65 or more
----------------------------------------------------------------
write a python program to represent the students seeking admissing in the university
Rules to Follows:
the details of student class are given below:
Class name:student
--Attribute:(private)
             student_id
             marks
             age
Methods
(public)_init_()
       create and intialize all instance  variables to none
validate_marks()
     if data is valid, return true.Else,return false
validate_age()
    check_qualification()         validate marks and age,
if valid,check if marks is 65 or more.
  variables to set its values
getter methods include getter methods for all instance
variables to get its value
continuing with the previous scenerio,a student eligible for admissioin has to choose a courseand pay
the fees for it.if they have scored more than85 marks in qualifing exam they get 25% discount on fees

valid course ids and fees are given below:

course id     fees
1001          25575.0
1002          15500.0'''

'''class student():
    def __init__(self,student_id,age,marks,course_id):
        self._student=student_id
        self._age=age
        self._marks=marks
        self._course_id=course_id
       
    def validate_age(self):
        if(self.age>20 and self.mark>=0 and self.mark<=100):
            return True
        else:
            return False
            
    def check_qualification(self):
        if(age>20 and marks>=65 and age<=100):
            return True
        else:
            return False

    def course(self,course_id,fees):
        if(self.marks>=85 and self.marks<=100):
            self.fees=(25/100)*self.fees
        if(self.qualification()):
            if(self.course_id==1001):
                self.fees=25575.0
                if(self.course_id==1002):
                        self.fees=15500.0
            return fees
s1=student(1001,21,89,456)
s1.course()'''
          


'''class Fun():
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
    def set_id(self,id):
        self.__s_id=id
    def get_id(self):
        return self.__s_id
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
  
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks  
        
    def valid_age(self):
        if(self.__age>20):
            return True
        else:
            return False
    def valid_marks(self):
        if(self.__marks>=0 and self.__marks<=100):
            return True
        else:
            return False
    def course(self,marks):
        d={"CSE":2554,"MECh":2555}
        if(marks>85):
            for i in d:
                d[i]=d[i]-d[i]*0.25
            print("The course is offered to you after discount of 25%",d)
        else:
            print("The course offered to u:",d)
    def valid_qualification(self):
        if(self.__marks and self.valid_marks() and self.valid_age() ):
            self.course(self.__marks)
            return True
        else:
            return False


s1=Fun()
s1.set_id(9)
s1.set_age(21)
s1.set_marks(89)
if(s1.valid_qualification()):
    print("Admission can be done")
else:
    print("admission can not be done")'''

'''


#qts--->3:

types=['small','medium','small','medium']
class Customer:
    def __init__(self, customer_name, quantity):
        self.customer_name=customer_name.title()
        self.quantity = quantity

    def validate_quantity(self):
        if self.quantity in range(1,6):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity


class PizzaService():
    counter = 100

    def __init__(self,customer,pizza_type,additional_topping):
        self.customer = customer
        self.pizza_type = pizza_type
        self.additional_topping = additional_topping
        self.pizza_cost = 0
        self.__service_id=None

    def validate_pizza_type(self):
        valid_types = ['small', 'medium']
        if self.pizza_type.lower() in valid_types:
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
            if self.pizza_type.title() == 'Small':
                self.pizza_cost = 150 * Customer.get_quantity(self.__customer)
                if self.additional_topping:
                    self.pizza_cost += 35 * Customer.get_quantity(self.__customer)
            if self.__pizza_type.title() == 'Medium':
                self.pizza_cost = 200 * customer.get_quantity(self.__customer)
                if self.additional_topping:
                    self.pizza_cost += 50 * Customer.get_quantity(self.__customer)
            if not self.__service_id:
                self.__service_id = self.__pizza_type[0] + str(pizzaservice.counter+1)
                pizzaservice.counter+=1
        else:
            self.pizza_cost = -1
        def get_service_id(self):
            return self.__service_id
        def get_pizza_type(self):
            return self.__pizza_type
        def get_customer(self):
            return self.__customer
        def get_additional_topping(self):
            return self.__additional_topping

class DoorDelivery(PizzaService):
    def __init__(self, customer,pizza_type, additional_topping, distance_in_kms):
        self.delivery_charge = 0
        self.distance_in_kms = distance_in_kms
        pizzaservice.__init__(self, customer,pizza_type, additional_topping)

    def validate_distance_in_kms(self):
        if self.__distance_in_km():
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost != -1:
                distance=1
                while(distance<=self.__distance_in_km):
                    if distance in range(1,6):
                        self.pizza_cost += 5
                    if distance in range(6,11):
                        self.pizza_cost += 7
        else:
            sef.pizza_cost = -1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_km(self):
        return self.__distance_in_km


c = Customer("Asha", 3)
p1 = PizzaService(c,"MEDIUM",True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1 = DoorDelivery(c,"MEDIUM",True, 6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())

'''


type=['small','medium','Small','Medium']
class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name.title()
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity is range(1,6):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity
class Pizzaservices:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in type:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
            if self.__pizza_type.title()=="Small":
                self.pizza_cost=150*Customer.get_quantity(self.__Customer)
                if self.__additional_topping:
                    self.pizza_cost+=35*Customer.get_quantity(self.__Customer)
            if self.__pizza_type.title()=="Medium":
                self.pizza_cost=200*Customer.get_quantity(self.__Customer)
            if not self.__service_id:
                self.__service_id = self.__pizza_type[0] + str(pizzaservice.counter+1)
                pizzaservice.counter+=1
        
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__additional_topping
class Doordelivery(Pizzaservices):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.delivery_charges=0
        self.__distance_in_kms=distance_in_kms
        Pizzaservices.__init__(self,customer,pizza_type,additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservices.calculate_pizza_cost(self)
            if self.pizza_cost!=-1:
                distance=-1
                while(distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost+=5
                    if distance in range(6,11):
                        self.pizza_cost+=7
                    distance +=1
        else:
            self.pizza_cost=-1
    def get_delivery_charge(self):
        return self.get_delivery_charge
    def get_distance_in_kms(self):
        return self.get_distance_in_kms
c=Customer("Ashu",3)
p1=Pizzaservices(c,"Medium",True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1=Doordelivery(c,"Medium",True,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())





