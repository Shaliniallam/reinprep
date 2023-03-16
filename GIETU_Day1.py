#Que 1
'''num =int(input("Enter a number :"))
print(num,type(num))
if (num % 3 == 0 and num %5==0):
    print("Multiple of 3 and 5")
elif(num % 5 == 0):
    print("Multiple of 5")
elif(num % 3==0):
    print("Multiple of both 3 ")
else:
    print("None")'''

#Que 2
'''#for loop
#num =int(input("Enter a Number :"))
for i in range(1,100):
    print(i,end=' ')
print()
#range(start,end,step)
for i in range(1,100,2):
    print(i,end=' ')
print()
for i in range(100,0,-1):
    print(i,end=' ')
print()
for i in range(100,1,-2):
    print(i,end=' ')
print()
for i in range(99,0,-2):
    print(i,end=' ')
print()
'''

#Que 3
'''#break
for i in range(1,101):
    if i == 51:
        break
    print(i,end=" ")
else:
    print("Else statement")
print()

#continue
for i in range(1,101):
    if i == 51:
        continue
    print(i,end=" ")
print()

#pass
for i in range(1,101):
    if i == 51:
        pass
    print(i,end=" ")
'''

#Que 4
'''#functions
def fun1():
    print("Function")
fun1()
def fun2(n1,n2):
    print("n1=",n1,"n2=",n2)
fun2(1,2)

#Addition
def fun3(n1,n2):
    n3 = n1+n2
    return n3
print("Value of n3=",fun3(20,30))

def fun4(n1,n2):
    n3=float(n1)+n2
    return n3
print("Value =",fun4(10,2.3))

def fun5(n1,n2):
    n3=float(n1)+n2
    return n3
print("Value =",fun5('10',2.3))
'''

#Que 5
'''def fun1(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
fun1(10,20,30,40)

def fun1(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
fun1(10,"20",30,40)

#Keyword argument
def fun2(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
fun2(num4=10,num3=20,num2=30,num1=40)
fun2(num3=10,num1=20,num4=30,num2=40)

#Default Argument
def fun3(name,rollno,branch,collagename):
    print(name,rollno,branch,collagename)
fun3("Sanjuuu",296,"CSE","GIETU")
fun3("Litu",45,"CSE","GIETU")

def fun4(name,rollno,branch,collagename="GIETU"):
    print(name,rollno,branch,collagename)
fun4("Sanjuuu",296,"CSE")
fun4("Litu",45,"CSE")

def fun5(name,rollno,branch="CSE",collagename="GIETU"):
    print(name,rollno,branch,collagename)
fun5("Mitra",12)
fun5("Sanju",296,"CSE")
fun5("Litu ",45,"CST")

#Overloading
def fun6(*var):
    for i in var:
        print(i,end=' ')
fun6(1,2,3)
print()
fun6(1,2,3,4)
print()
fun6(1,2,3,4,5)
print()

def add(*var):
    sum=0
    for i in var:
        sum=sum+i
    return(sum)
print(add(10,2))
print(add(10,2,3))
print(add(10,2,3,4))
'''

#Que 7
'''n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
n3=int(input("Enter 3rd number : "))
if n1==7:
       print(n2*n3)
elif n2==7:
    print(n3)
elif n3==7:
    print("-1")
else :
    print(n1*n2*n3)
'''

#Que 8
'''def cc(amINR,curr):
    if curr=="Euro":
        print(amINR*0.01417)
    elif curr =="BP":
        print(amINR*0.0100)
    elif curr=="AD":
        print(amINR*0.02140)
    elif curr=="CD":
        print(amINR*0.02027)
    else:
        print("-1")
cc(300,"Euro")
cc(300,"BP")
cc(300,"AD")
cc(300,"CD")
'''

#Que 9
'''n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
n3=int(input("Enter 3rd number : "))
if n1==7:
       print(n2*n3)
elif n2==7:
    print(n3)
elif n3==7:
    print("-1")
else :
    print(n1*n2*n3)
'''

#Que 10
'''ap=int(input("Enter no.of Adults :"))
cp=int(input("Enter no.of Child :"))
#adult = 37550.0
#child = 1/3 of adult
#ticket=cost + 7%tax
#last price = ticket - 10%

ap=int(input("Enter no.of Adults :"))
cp=int(input("Enter no.of Child :"))
total=((ap*37550.0)+(cp*3755.0))
print(total)
total1=total*0.7
total2=total+total1
print("With Service Tax= ",total2)
fp=total2 * 0.90
print(fp)
'''

