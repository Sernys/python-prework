# Question #1 
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as, def hello_name(user_name): 

def hello_name(user_name):
    print("hello_" + user_name +"!")
hello_name("username".upper())

# Question #2  
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
list_odds=[] #<--- to have it organize 
def first_odds():
    for odd in range(1,100,2): 
        list_odd = odd
        list_odds.append(list_odd)
    print(list_odds)
    return None   
first_odds()

# Question #3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as  def max_num_in_list(a_list):

def max_num_in_list(a_list):
    print(max(a_list)) #<--- it will print the biggest number
 
a_list = [45,56,76,92,3] #<-- list given
max_num_in_list(a_list)

# Question #4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 != 0:#<-- when is not divisible by 4
        return False  
    elif a_year % 100 == 0 and a_year % 400 != 0:#<-- when is not divisible by 100 or 400
        return False 
    else:
        return True #<--- this will show if divisible by all of them 
a_year = int(input("Enter the year: ")) #<--- Enter the year and it will let you know if it is a leap year or not
is_leap_year(a_year)#<-- this will execute the year given

# Question #5 
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.  
def is_consecutive(a_list):
 if sorted(a_list) == list(range(min(a_list),max(a_list)+1)):#<--- this will check if the list is consecutive and it will choose execute True or False
    return True
 else:
    return False #<-- it will print if the list is not consecutive
a_list = [1,2,3,5,8]#<-- list given 
print(is_consecutive(a_list))