#SELECTION SORT
#qts-->1
'''
def selectionSort(array,size):
    for step in range(size):
        min_idx=step

        for i in range(step + 1,size):
            if array[i]<array[min_idx]:
                min_idx=i

        (array[step],array[min_idx])=(array[min_idx],array[step])

data=[20,12,10,15,2]
size=len(data)
selectionSort(data,size)
print('sorted array in ascending order:')
print(data)
 '''   
#qts-->2
'''Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, India.40 min
They want to keep track of customers who buy fruits from them and also the billing process.


Write a python program to implement the class diagram given below.

RULES TO FOLLOW
=================
Class Description:
Fruit Info class:
fruit_name_list: Static list which contains the list of fruits available
fruit_price_list: Static list which contains the price/kg of fruits
The above two lists have one-to-one correspondence, initialize it with the data given in the table
get_fruit_price(fruit_name): Accept a fruit name and return its price/kg. If fruit is not available, return -1

Fruit Name	Apple	Guava	Orange	Grape	Sweet Lime
Price per Kg	200	80	70	110	60Purchase class:
Initialize static variable counter to 101
calculate_price(): Calculate and return total fruit price based on rules given below
For valid fruit name (hint: invoke get_fruit_price(fruit_name)),
Calculate price based on price/kg and quantity of the fruit purchased by the customer
If price/kg of the fruit is maximum among the fruits in fruit lists and quantity purchased is more than 1kg, apply 2% discount on calculated price
If price/kg of the fruit is minimum among the fruits in fruit lists and quantity purchased is 5kg or more, apply 5% discount on calculated price
If the customer is a "wholesale" customer, provide an additional 10% discount. Apply this discount on already discounted price, 
if any one of the above two points are applicable. Else apply it on calculated price
Auto-generate purchase id starting from 101 prefixed by “P”. Example – P101,P102 P103 etc.
Return final fruit price
Else, return -1.
Note:
Perform case sensitive string comparison 
There will be only one fruit with maximum price and one with minimum price

For testing:
Create objects of Customer and Purchase class
Invoke calculate_price() on Purchase object
Display the details

class FruitInfo:
    fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            index = FruitInfo.fruit_name_list.index(fruit_name)
            return FruitInfo.fruit_price_list[index]
        else:
            return -1


class Purchase:
    counter = 101

    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = 'P' + str(Purchase.counter)
        Purchase.counter += 1
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity

    def calculate_price(self):
        price_per_kg = FruitInfo.get_fruit_price(self.__fruit_name)
        if price_per_kg == -1:
            return -1

        total_price = price_per_kg * self.__quantity

        if price_per_kg == max(FruitInfo.fruit_price_list) and self.__quantity > 1:
            total_price *= 0.98  # 2% discount
        elif price_per_kg == min(FruitInfo.fruit_price_list) and self.__quantity >= 5:
            total_price *= 0.95  # 5% discount

        if self.__customer == 'wholesale':
            total_price *= 0.9  # 10% discount

        return total_price

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_fruit_name(self):
        return self.__fruit_name

    def get_quantity(self):
        return self.__quantity


class Customer:
    def __init__(self, customer_name):
        self.__customer_name = customer_name

    def get_customer_name(self):
        return self.__customer_name


# Testing
customer1 = Customer('John')
purchase1 = Purchase(customer1.get_customer_name(), 'Apple', 2)
print(purchase1.calculate_price())  # Expected output: 392.0

customer2 = Customer('Jane')
purchase2 = Purchase(customer2.get_customer_name(), 'Grape', 6)
print(purchase2.calculate_price())  # Expected output: 627.0

customer3 = Customer('Peter')
purchase3 = Purchase(customer3.get_customer_name(), 'Mango', 4)
print(purchase3.calculate_price())  # Expected output: -1

'''





#qts--->3

'''
The owner of a BakeHouse wants to keep track of the tables 
that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed from the list.

BakeHouse
- occupied_table_list
init()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class. 
Represent occupied_table_list using an appropriate data 
structure.


Note: Table numbers should be maintained in ascending order in the occupied_table_list.


Tables should be allocated and de-allocated as mentioned in the example below:

Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should be allocated table 5 and the table list should be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated and the next new customer should be allocated table 2 as it is the first free table.


Implement the allocation logic in allocate_table() method and de-allocation logic in deallocate_table() method.



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SortList:  
    #Represent the head and tail of the singly linked list  
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
          
    #addNode() will add a new node to the list  
    def addNode(self, data):  
        #Create a new node  
        newNode = Node(data);  
          
        #Checks if the list is empty  
        if(self.head == None):  
            #If list is empty, both head and tail will point to new node  
            self.head = newNode;  
            self.tail = newNode;  
        else:  
            #newNode will be added after tail such that tail's next will point to newNode  
            self.tail.next = newNode;  
            #newNode will become new tail of the list  
            self.tail = newNode;


    #sortList() will sort nodes of the list in ascending order  
    def sortList(self):  
        #Node current will point to head  
        current = self.head  
        index = None;  
        l=[] 
        if(self.head == None):  
            return;  
        else:  
            while(current != None):  
                #Node index will point to node next to current  
                index = current.next;  
                  
                while(index != None):  
                    if(current.data > index.data):  
                        temp = current.data;  
                        current.data = index.data;  
                        index.data = temp;  
                    index = index.next;  
                current = current.next;  
                l.append(index)
    #display() will display all the nodes present in the list  
    def display(self):  
        #Node current will point to head 
        current = self.head
        if(self.head == None):  
            print("List is empty");  
            return;  
        while(current != None):  
            #Prints each node by incrementing pointer  
            print(current.data)  
            current = current.next
        return " "
    def replace(self,data):
        current = self.head
        while(current.next.next != None):
            current = current.next
        current.next.item=data
        return current.next.item
    def deallocation(self,x):
              if self.head is None:
                  print("The list has no element to delete")
                  return
              if self.head.data==x:
                  self.head=self.head.next
                  return
              n=self.head
              while n.next is not None:
                  if n.next.data==x:
                      break
                  n=n.next
              if n.next==None:
                  print("item not found in the list")
              else:
                  n.next=n.next.next
    def allocation(self,index,data):
        if index==1:
            Newnode=Node(data)
            Newnode.next=self.head
            self.head=Newnode
        i=1
        n=self.head
        while i<index-1 and n is not None:
            i+=1
            n=n.ref
        if n is None:
            print("index out of range")
        else:
            Newnode=Node(data)
            Newnode.next=n.next
            n.next=Newnode
        
        
              
sList = SortList();    
sList.addNode(9);  
sList.addNode(7);  
sList.addNode(2);  
sList.addNode(5);  
sList.addNode(4);  
print(sList.display())  
sList.deallocation(2)
print(sList.display()) 
sList.allocation(2,2)
print(sList.display())

'''
#qts-->4
'''
A teacher is conducting a camp for a group of five children.
 Based on their performance and behavior during the camp, the
 teacher rewards them with chocolates.
Write a Python function to Find the total number of chocolates
received by all the children put together.
Assume that each child is identified by an id and it is stored
 in a tuple and the number of chocolates given to each child
 is stored in a list.
The teacher also rewards a child with few extra chocolates 
for his/her best conduct during the camp.
If the number of extra chocolates is less than 1, an error 
message "Extra chocolates is less than 1", should be 
displayed.
If the given child Id is invalid, an error message 
"Child id is invalid" should be displayed. Otherwise,
 the extra chocolates 
provided for the child must be added to his/her existing 
number of chocolates and display the list containing the
 total number of chocolates received by each child.


child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

functions

calculate_total_chocolates()

reward_child(child_id_rewarded,extra_chocolates)


class ChocolateCamp:
    def __init__(self, child_id, chocolates_received):
        self.child_id = child_id
        self.chocolates_received = chocolates_received
    
    def calculate_total_chocolates(self):
        total_chocolates = sum(self.chocolates_received)
        return total_chocolates
    
    def reward_child(self, child_id_rewarded, extra_chocolates):
        if extra_chocolates < 1:
            print("Extra chocolates is less than 1")
            return
        try:
            index = self.child_id.index(child_id_rewarded)
            self.chocolates_received[index] += extra_chocolates
        except ValueError:
            print("Child id is invalid")
            return
        print("Updated chocolates received list:", self.chocolates_received)


child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

camp = ChocolateCamp(child_id, chocolates_received)
print("Total chocolates received by all children:", camp.calculate_total_chocolates())

camp.reward_child(20, 3)  
camp.reward_child(60, 5)
camp.reward_child(30, -2)


'''

# Python program for implementation of Quicksort Sort
'''
def partition(array, low, high):

	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

# function to perform quicksort
def quickSort(array, low, high):
	if low < high:

		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)
		

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)

'''

#qts--->5
'''

Write a python program that accepts a text and displays a 
string which contains the word with the largest frequency
 in the text and the 
frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose 
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a 
single space between the words.
Perform case insensitive string comparisons wherever 
necessary.
'''


class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, word, freq):
        new_node = Node(word, freq)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.word, current_node.freq)
                current_node = current_node.next

text = input("Enter some text: ")

# Convert the text to lowercase
text = text.lower()

# Split the text into words
words = text.split()

# Create a linked list to store the frequency of each word
linked_list = LinkedList()
for word in words:
    current_node = linked_list.head
    while current_node is not None:
        if current_node.word == word:
            current_node.freq += 1
            break
        current_node = current_node.next
    else:
        linked_list.insert(word, 1)

# Find the word with the largest frequency
max_freq = 0
max_word = ""
current_node = linked_list.head
while current_node is not None:
    if current_node.freq > max_freq:
        max_freq = current_node.freq
        max_word = current_node.word
    elif current_node.freq == max_freq:
        if len(current_node.word) > len(max_word):
            max_word = current_node.word
    current_node = current_node.next

# Display the result
print(max_word, max_freq)































