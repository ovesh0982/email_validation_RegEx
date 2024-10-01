print("Email_validation_RegEx")
# first_condition = a-z  oveshaziz123@gmail.com
# first_condition = 0-9
# first_condition = . _ time 1
# first_condition = @ time 1
# first_condition = . 2,3 position pe hona chaiye


import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\W+[.]\w{2,3}$"
user_emai = input("Enter your Email: ")

if re.search(email_condition,user_emai):
  print("Right Email")
else:
  print("wrong Email")