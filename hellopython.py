import random
import sys
import os

print("hello")

# Comment

'''
Multiline
'''

name = "Albert9000"
print(name)

'''
Datatypes:
Numbers Strings Lists Tuples Dictionaries
'''

#Numbers
print("5 + 2 = ",5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)

print("1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2)
print("(1 + 2 - 3 * 2 = ", (1 + 2 - 3) * 2)

#strings
quote = "\"this is a quote"

multi_live_quote = '''just
like everyone else'''

new_string = quote + multi_live_quote

print("%s %s %s" % ('I like the quote', quote, multi_live_quote) )
#have 5 new lines
print("\n" * 5)
#end="" removes the newlines between prints
print("I don't like ", end="")
print("newlines")

#Lists
grocery_list =['Juice', 'Tomatoes', 'Potatoes',
               'Bananas']

print("First Item:", grocery_list[0])
#update an item in the list
grocery_list[0] = "Green Juice"
print("First Item:", grocery_list[0])
#print specific items from the list:
print(grocery_list[1:3])

other_events = ['Wash car', 'Pick up kids', 'Cash check']
#lists inside of lists
to_do_list = [other_events, grocery_list]

print(to_do_list)
print(to_do_list[1][3])
#Add item to end of the list
grocery_list.append('Onions')

#Insert item into list
grocery_list.insert(1, "Pickle")
#remove a specific item in list
grocery_list.remove("Pickle")
#Sort
grocery_list.sort()
#reverse sort
grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

#Another way to merge lists
to_do_list2 = other + grocery_list
#Grab the number of items in a list
print(len(to_do_list2))
#get the Highest item in a list
print(max(to_do_list2))
#get the lowest item in a list
print(min(to_do_list2))

#Tuples
#Unlike lists you cannot change the data after you've created it

pi_tuple =  (3,1,4,1,5,9)
#convert a tuple into a list
new_tuple = list(pi_tuple)
#convert a list into a tuple
new_list = tuple(new_tuple)

len(tuple)
min(tuple)
max(tuple)

#Dictionaries
