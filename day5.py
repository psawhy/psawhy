# total = 0
# for number in range(1,101):
#     total +=number
# print(total)


# ------bakhsh paziri------- 

# target =100 
# for number in range(1 , target + 1):
#     if number % 3 ==0 and number % 5 == 0 :
#         print("fizzBuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)

# password----------------
import random
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("wellcome to the pypassword generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbol= int(input(f"How many symbol would you like?\n"))
nr_number= int(input(f"How many number would you like? \n"))

password_list =[]

for char in range(1 ,nr_letters + 1):
    password_list.append(random.choice(letters))
    
for char in range(1 , nr_symbol +1):
    password_list += random.choice(symbols)

for char in range(1 , nr_number +1 ):
    password_list +=random.choice(numbers)


random.shuffle(password_list)


password= ""
for char in password_list:
    password += char

print(f"Your password is : {password}")