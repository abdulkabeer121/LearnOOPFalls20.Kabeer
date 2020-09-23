# Today we will learn how may and what are te data types in python

user_name = "ABDULKABEERABID"       # Creating a String Data type
age = 20                            # Creating an Int Data type
roll_no = "bdsm-s20-005"            # Creating a string Data type (Anything writtin in "".... Python interpreter consider it as a string value)
marks_list = [20, 30, 40, 50, 60]   # Creating a List Data type

#----------------------------------------------------------------------------------------------------------------------------------------------
# Printing the above variables

print (user_name)
print (age)
print (roll_no)
print (marks_list)
print (marks_list[0] , marks_list[1] , marks_list[2] , marks_list[3] , marks_list[4])

#----------------------------------------------------------------------------------------------------------------------------------------------
# Creating a list of Different data types

any_list = ["abdulkabeerabid", 20 , "bdsm-s20-005"]
print (any_list)
print ("\nMy name is: " + any_list[0])
print ("My age is: " + str(any_list[1]))
print ("my rollno is: " + any_list[2])

#----------------------------------------------------------------------------------------------------------------------------------------------
# Difference between int and string

n1 = 13
n2 = 17

n3 = n1 + n2                       # Here n1 and n2 are considered as int
n4 = str(n1) + str(n2)             # Here n1 and n2 are considered as string

print ("\n")
print (n1)
print (n2)
print (n3)
print (n4)

#----------------------------------------------------------------------------------------------------------------------------------------------

