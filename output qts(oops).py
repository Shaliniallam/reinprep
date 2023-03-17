#qts----->1

'''class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())'''



#qts----->2

'''class Customer:
    def __init__(self):
        self.cust_id = 100
c1=Customer()
print(c1.cust_id)
class Customer:
    def __init__(self,id):
        self.id = 100
c1=Customer(200)
print(c1.id)'''

#qts--->3

'''class book:
    def __init__(self):
        self.title=None
my_fav=book()
my_fav.title="head first prgmng"
your_fav=book()
your_fav.title="learn python the hard way"
my_fav.title="learning python"
print("my fav is",my_fav.title)
print("your's is",(your_fav.title))'''

#qts--->4
'''class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=shoe(1000,"canvas")
print(s1.price,s1.material)'''


#qts--->5
'''class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=shoe(1000,"canvas")
print("the unique if of the object",id(s1))'''


#qts------>6

'''class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return"shoe with price:"+str(self.price)+"and material:"+self.material
s1=shoe(1000,"canvas")
print(s1)'''

#qts--->7
'''class Mobile:
    def _init_(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("calculating price")
Mobile().purchase()
Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
m1=m2
print(m1)
print(m2)'''

#qts---->8
'''class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
        self.total_price = None
    def purchase(self):
        if self.brand =="apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price *(discount / 100)
        print("total price of",self.brand,"mobile is",self.total_price)
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()'''

#qts---->9
'''class Customer:
    def _init_(self,cust_id,name,age,wallet_balance):
        self.cust_id =cust_id
        self.name = name
        self.age=  age
        self.wallet_balance=wallet_balance
    def update_balance(self,amount):
       if amount<1000 and amount >0:
           self.wallet_balance+=amount
    def show_balance(self):
        print("the balance is",self.wallet_balance)
c1=Customer(100,"Gopal",24,1000)
c1.show_balance()'''


#qts---->10
'''class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_balance(self,amount):
        if amount < 50000 and amount > 0:
            self.__wallet_balance += amount
    #def show_balance(self):
            #print("The balance is",self.__wallet_balance)
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Aaru",25,1000)
print(c1.get_wallet_balance())
#c1.update_balance(500)
c1.show_balance()#
c1.get_wallet_balance
#print(c1._wallet_balance)..._wallet_balance gives error 
c1.set_balance(5000)
print(c1.get_wallet_balance())'''


#qts---->11
'''class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam Length",dam1.get_length())'''


#qts---->12



#qts--->13

'''class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000'''
#qts---->14

class Table:
    def __init__(self):
	    self.no_of_legs=4
	    self.glass_top=None
	    self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(id(dining_table),id(back_table),id(front_table))
        




























