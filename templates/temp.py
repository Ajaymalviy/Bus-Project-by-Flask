# # string="the broad road street"
# # for i in range(len(string)):
# #     if i=='r' and i+1=='o'and i+2=='a' and i+3=="d":
# #         x=string.replace("road",'rd')
# #         print(x)   
      
# # import re
# # string="the broad road street"
# # string1=re.sub(r'\broad \b','rd',string)
# # print(string1)
# # # if string:
# # #     string.replace("road",'rd')
# # #     print(string)
# # import re

# # txt = "The rain in Spain"
# # x = re.search("^The.*Spain$", txt)
# # if x :
# #     print(x)
# number=int(input("enter any number:"))
# x=str(number)
# # print(len(x))
# if len(x)==10:
#     if x[0]<6:
#         print("enter a number which start with greater than 5:")
#     else:
#         print("this is valid number: " +x)    
# elif len(x)>10 and  len(x)<13:
#     if x[0] == '+' or (x[0] == "9" and x[1] == '1'):
#         if x[0]<6 or x[1]<6:
#             print("first number be greater than haven:")
#         else:
#             print("This  is a mobil number:"+x)
#     else:
#         print("this is invalid input:") 
import re

number = input("Enter any number: ")
pattern = re.compile(r'^([6-9]\d{9}|(\+91)?\d{10}(\d{3})?)$')

if pattern.match(number):
    if number[0] in "6789":
        print("This is a valid number and starts with a digit greater than 5:", number)
    elif number.startswith("+91"):
        print("This is a valid number and starts with +91:", number)
else:
    print("This is an invalid input.")



