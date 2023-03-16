#Que1

'''Paired Outputs
Problem statement:For each number in list_b get the number and its position(Index)
in mylist as are turn list of tuples.
Input:
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]

Output:
[(6, 2), (4, 8), (6, 2), (1, 3), (2, 7), (2, 7)]

#List
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)

print([(i,mylist.index(i))for i in list_b])

#dict
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
dict={}
for i in list_b:
    dict[i]=mylist.index(i)
print(dict)

print({i:mylist.index(i)for i in list_b})'''

#Que2
'''Problem statement: The goal is to tokenize the following 5sentences into words,
excluding the stop words.
sentence = ["a new world record was set",
            "in the holy city ayodhya",
            "on the eve of diwali on tuesday",
            "with over three lakh diya or earthen lamps",
            "lift up simantanouesly on the banks of the sarayu river"]
stopwords = ['for','a','of','the','and','to','in','on','with','was']


sentence = ["a new world record was set",
            "in the holy city ayodhya",
            "on the eve of diwali on tuesday",
            "with over three lakh diya or earthen lamps",
            "lift up simantanouesly on the banks of the sarayu river"]
stopwords =['for','a','of','the','and','to','in','on','with','was']
result=[]
for i in sentence:
    data=[]
    for j in i.split():
        if j not in stopwords:
            data.append(j)
    result.append(data)
print(result)
print()

print([[j for j in i.split() if j not in stopwords]for i in sentence])'''

#Que3
'''
Input: A string of comma seperated numbers.the number 5 and 8 are present
in the list. Assume that 8 always comes after 5,
Case1: num1=add all the numbers which do not lie btw 5 and 8 in the input.
Case2: num2=number formed by concatenating all numbers from 5 to 8.
Output: Sum of num1 and num2
Example: 3,2,6,5,1,4,8,9
num1 = 3+2+6+9=20
num2 = 5148
Output = 5148+20=5168

values = list(map(int,input().split(",")))
num1 = sum(values[:values.index(5)])+sum(values[values.index(8)+1:])
print("num1 =",num1)
l = values[values.index(5):values.index(8)+1]
num2 = " "
for i in l:
    num2+=str(i)
print("num2 =",int(num2))
print(int(num2),"+",num1,"=",int(num2)+num1)'''

#Que4,cgb 
#String Rotation
'''
input: rhdt:246,ghftd:1246
exp1:here every string is associated with the number sep by:
--->if sum of squares of digits is even then rotate the string by 1
--->if sum of squares of digits is odd then rotate the string left by 2 position
2*2+4*4+6*6=56 which is even so rotate rhdt=trhd
1*1+2*2+4*4+6*6=57 which is odd so rotate left by 2:ghftd=ftdgh

test_list = ["rhdt","ghftd"]
print ("Original list : " + str(test_list))
test_list = test_list[3:] + test_list[:3]
print ("List after left rotate by 3 : " + str(test_list))
test_list = test_list[-3:] + test_list[:-3]
print ("Rotational String :"+ str(test_list))


s=input()
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=list(str(n))
    s=0
    print(n)
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))
'''

#Que5
#Sum of largest prime factors
'''Given  number n,write a program to find the sum of largest prime factor
of each of nine consecutive numbers starting from n.
g(n)=f(n)+f(n+1)+f(n+2)+f(n+3)+f(n+4)+f(n+5)+f(n+6)+f(n+7)+f(n+8)
where,g(n) is the sum add f(n) is the largest prime factor of n
for example
g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
     =5+11+3+13+7+5+2+17+3
     =66
'''
'''def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def lpf(num):
    if num < 2:
        return None
    for i in range(int(num ** 0.5), 1, -1):
        if num % i == 0 and is_prime(i):
            return i
    return num

def sum_lpf(n):
    result = 0
    for i in range(n, n + 9):
        result += lpf(i)
    return result'''









































    
        














    
