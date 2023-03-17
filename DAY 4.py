#Que 1
'''Write a python function,nearest_palindrome() which accepts a number and
returns the nearest palindrome greater than the given number.

      Sample Input             Output
            99                  101
           1221                1331
'''


'''import sys
def Next_smallest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(Next_smallest_palindrome(99))
print(Next_smallest_palindrome(1221))'''



#Qts 2
'''care hospital want to know the medical speciality visited by the ma no.of patients.assume that the patient id
of the patient along with the medical speciality visited by the patient is stored in a list.
The details of the medical specialities are stored in dictionary as follows:
{"p":"pediatrics","o":"orthopedics","E":"ENT"}
write a fun to find the medical speciality visisted by the max no.of patients and return the name of the speciality. 
Note 1: Assume that there is always only one medical speciality which is visited
by maximun number of patients and return the name of the speciality.
Note 2: 
Perform case sensitivite string comparasion wherever necessary.

    Sample Input                              Expected Output
[101,P,102,O,302,P,305,P]                        Pediatrics
[101,P,102,O,302,P,305,E,401,0,656,O]            Orthopedics
[101,P,102,O,302,P,305,P,401,E,656,O,987,E]      ENT'''

'''def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    max_visit=0

    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality= medical_speciality['P']
    elif E>O:
        speciality= medical_speciality['E']
    else:
        speciality= medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'P',302,'P',305,'P',401,'E',656,'E']

medical_speciality={"P":"pediatrics","O":"orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)'''
        

#qts 3
'''write apython function to display all the commom characters btw two strings.Return -1 if thre are nomaching characters.
note:ignore blank spaces if there are any.
perform case sensitivity string comparision whenever necessary.

sample input:                               output:
"I like python"                             lieyon
"java is a very popular language"


string1 = "I like python"
string2 = "java is a very popular language"

result = common_characters(string1, string2)
print(result)'''


def common_characters(str1, str2):
  
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    common = ""
    for char in str1:
        
        if char in str2 and char not in common:
            
            common += char
    if len(common) > 0:
        return common
    else:
        return -1
string1 = "I like python"
string2 = "java is a very popular language"

result = common_characters(string1, string2)
print(result)

