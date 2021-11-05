import num_funcs

print ("please select an option: ")
print("[1] Equal\n [2] Lower \n [3] Ggeater \n [4] In range \n [5] Even \n [6] Odd \n [7] In List")
option= int(input('select option: '))
if option == 1:
    if num_funcs.is_equal(5,7):
    print("your number is equal")
else :
    print("your number is not equal")
elif option ==2:
    num_funcs.is_lower(5,7)
elif option ==3:
    num_funcs.is_greater(5,7)
elif option ==4:
    num_funcs.is_in_range(5,7)
elif option ==5:
    num_funcs.is_even(5,7)
elif option ==6:
    num_funcs.is_odd(5,7)
elif option ==7:
    num_funcs.is_in_list(5,7)
print ("please enter the first number: ")
num_1= input()
print ("please enter the second number: ")
num_2= input()
