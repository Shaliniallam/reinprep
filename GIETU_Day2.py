#List
'''list=[]
print(list,type(list))

list1=[10,20.2,True,"Litu"]
print(list1,type(list1))

list2=[10,20,30,40,50]
list2.append(100)
print(list2,type(list2))

list2.insert(2,22)#index,value
print(list2,type(list2))

list2.remove(40)
print(list2,type(list2))

list2.pop()
print(list2,type(list2))

list2.pop(0)
print(list2,type(list2))

del list2[1]#index
print(list2,type(list2))'''


'''1.WAP function which accepts a sentence and finds the no.of letters and digits in the sentence. It should return a list in which the first value should the lettrs count and second value should be digit count.
Ignore the spaces or any other special character in the sentence.

Sample Input      Expected Output
Sanjuuu 296        [7,3]
qwerty             [7,0]

countSL.py
#Count no.of letters and digits
def count(n):
    lc = 0
    dc = 0
    for i in n:
        if i.isalpha():
            lc=lc+1
        elif i.isdigit():
            dc=dc+1
        else:
            continue
    return[lc,dc]
print(count("Sanjuu 296"))


============================================================
2.WAP function find_pairs_of_numbers() which accepts a list of postive integers with no repetations and returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.

Sample Input               Expected Output
[1,2,7,4,5,6,0,3],6           3  (1,5)(2,4)(6,0)
[3,4,1,8,5,9,0,6],9           4  (3,6)(4,5)(1,8)(9,0)

ponum.py
def ponum(num_list,n):
    count=0
    for i in num_list:
        index = num_list.index(i)+1
        for j in range(index,len(num_list)):
            if i+num_list[j]==n:
                count+=1
                #count=count+1
    return count
num_list=[2,4,8,3,0,5,6,9]
n=6
print(ponum(num_list,n))

==========================================================

3.WAP function which accepts a string and returns a string made of the first 2 and the last 2 characters of the given string.If the string length is less than 2, return -1.

strlen.py
def str(n):
    if len(n)<2:
        print(-1)
    else:
        return n[0:2]+n[-2:]
print(str("qwerty5"))
print(str("r"))


=========================================================
4. WAP function to add 'ing' at the end of the given string and return the new string. If the given string and return the new string. If the given string already ends with 'ing' then add 'ly'. If the length of the given string is less than 3,leave it unchanged.

addIng.py
def add(str):
    length = len(str)
    if length>3:
        if str[-3:]=='ing':
            str += 'ly'
        else:
            str += 'ing'
    return str
print(add("fly"))
print(add("Stand"))

==========================================================
5.WAP function,which accepts a whole number and returns True if it satisfies the given conditions.
  ->The number and its double should haave exactly the same number of digits.
  ->Both the numbers should have the same digits,but in different order.
Otherwise it should return False.

Example:--> 125874 to 251748

chkdouble.py
def chkdble(num):
    num1=str(num*2)
    num=str(num)
    print(num1)
    count=0
    for i in num:
        if i in num1:
            count += 1
        else:
            return False
            break
    if count == len(num):
        return True
print(chkdble(125874))
print(chkdble(121))
==========================================================
6.A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project by assessment. Assume that the marks of her 10students are avaliable in a tuple. The marks are out of 25.
WAP to implement the following functions:-
i)find average():-Find the return the percentage of students who have scored more than the avarage mark of the class.
ii)generate_frequency():- Find how many students have scored the same marks. The result should be populated in a list and returned.
iii)sort_marks():-Sort the marks in the increasing order from 0 to 25. The sorted value should be populated in a list and returned.

Sample Input : (2,18,25,24,2,5,18,20,20,21)
Expected Output: 70.0

stdmarks.py
num = [2,18,25,24,2,5,18,20,20,21]
avg = sum(num)/len(num)
print("Average", round(avg,1))

list = ['2','18','25','24','2','5','18','20','20','21']
freqy = {}
for i in list:
   if i in freqy:
      freqy[i] += 1
   else:
      freqy[i] = 1
print(freqy)
==========================================================
7. Translate
translate.py

def translate(dict1,english):
   swedish=[]
   for i in english:
       swedish.append(dict1[i])
   return swedish
dict1= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english=["merry","christmas"]
swedish=translate(dict1, english)
print(swedish)
==========================================================
8. Find the no.of distinct subarrays in an array of position integers such that sum of the subarrays is an odd integers,two subarrays are considered different if they start or end at different index input. 

1
3
1 2 3
[1] [1 2] [1 2 3] [2] [2 3] [3]
4

subarr.py
n1 = int(input("n1 : "))
n2 = int(input("n2 : "))
array=[i for i in range(n1,n2+1)]
print(array)
list=[array[i:j+1] for i in range(len(array))for j in range(i,len(array))]
print(list)
c=0
for i in list:
    if sum(i)%2!=0:
        c+=1
print(c)'''
=========================================================

