# python program to a simple calculator


# add 
def add(num1,num2):
     return num1 + num2 

# substract 
def sub(num1,num2):
     return num1 - num2 

# multiply 
def multiply(num1,num2):
     return num1 * num2  

# divide 
def divide(num1,num2):
     return num1 / num2 

# average
def avg(num1,num2):
     return (num1 + num2)/2  

 # user input 
print("Please select a operation:\n " \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n") 

select = int(input("Select a operation from 1,2,3,4,5: ")) 

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))


 # Print the result 

if select == 1:
     print(number1, "+", number2, "= ", \
           add(number1, number2))
     
elif select == 2:
     print(number1, "-", number2, "= ", \
           sub(number1, number2)) 
     
elif select == 3:
     print(number1, "*", number2, "= ", \
           multiply(number1, number2))
     
elif select == 4:
     print(number1, "/", number2, "= ", \
           divide(number1, number2))

elif select == 5:
     print("(",number1, "+", number2, ")", "/", "2", "= ", \
           avg(number1, number2)) 
    
else:
     print("Invalid operation! Pls select again!")