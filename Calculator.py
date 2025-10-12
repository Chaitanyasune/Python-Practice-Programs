# Program to calculate ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, PERCENTAGE 

# Taking Inputs from user 

def check_input():

    # Checking User Inputs
   
    try:
        a = float(input("Enter First Number"))
        print()
        b = float(input("Enter Second Number"))
        print()
        
        if a < 0 and b < 0:
            print("Your Input is Valid Negative Number")
            print()
        elif a >= 0 and b >= 0:
            print("Your Input is Valid Positive Number")
            print()
            select_operation(a,b)

    except ValueError as e:
        print("Numbers cannot be special characters",e)


# This function is for ADDITION:


def addition(a,b):
    try:
        print('Your First Number is :',a)
        print()
        print('Your Second Number is :',b)
        print()
        print("Calculating ADDITION")
        print()
        
        return a + b
    except Exception as e:
        print("Error in ADDITION FUNCTION",e)


# This function is for SUBTRATION:

def subtration(a,b):
    try:
        print('Your First Number is :',a)
        print()
        print('Your Second Number is :',b)
        print()
        print("Calculating SUBTRATION")
        print()
        return a - b
        
    except Exception as e:
        print("Error in SUBTRATION FUNCTION",e)


# This function is for MULTIPLICATION:

def multiplication(a,b):
    try:
        print('Your First Number is :',a)
        print()
        print('Your Second Number is :',b)
        print()
        print("Calculating MULTIPLICATION")
        print()
        return a * b
    
    except Exception as e:
        print("Error in MULTIPLICATION FUNCTION",e)



# This function is for DIVISION:

def division(a,b):
    try:
        try:
            print('Your First Number is :',a)
            print()
            print('Your Second Number is :',b)
            print()
            print("Calculating DIVISION")
            print()
            return a / b
                
        except ZeroDivisionError as e:
            print("You cannot divide a Number by Zero",e)
            
    except Exception as e:
        print("Error in DIVISION FUNCTION",e)


# This function is for PERCENTAGE:

def percentage(a,b):
    try:
        print('Your First Number is :',a)
        print()
        print('Your Second Number is :',b)
        print()
        print("Calculating PERCENTAGE")
        print()
        return (a * 0.01) * b
        
    except Exception as e:
        print("Error in PERCENTAGE FUNCTION",e)
        


#This function CalculateS ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, PERCENTAGE


def select_operation(a,b):
    
    try:
        print("Please select operation -\n"
              "\n"
              "Press A or 1 for ADDITION\n"
              "Press S or 2 for SUBTRATION\n"
              "Press M or 3 for MULTIPLICATION\n"
              "Press D or 4 for DIVISION\n"
              "Press P or 5 for PERCENTAGE\n"
              "Press E or 6 to EXIT\n")
       
        var_op = input("Select Operation : ").strip().upper()
        print()
        

        
        # print(f"Operation Selected : is {var_op} which is for {var}")
        # print("Operation Selected is : ",var_op)
        # print(type(var_op))
        
 
        if var_op == '1' or var_op == "A":
            print(f"Operation Selected is : '{var_op}' which is for ADDITION")
            print()
            print(f"ADDITION OF {a} + {b} IS", addition(a,b))
            print()
            
        elif var_op == '2' or var_op == "S":
            print(f"Operation Selected is : '{var_op}' which is for SUBTRATION")
            print()
            print(f"SUBTRATION OF {a} - {b} IS", subtration(a,b))
            print()
            
        elif var_op == '3' or var_op == "M":
            print(f"Operation Selected is : '{var_op}' which is for MULTIPLICATION")
            print()
            print(f"MULTIPLICATION OF {a} * {b} IS", multiplication(a,b))
            print()
            
        elif var_op == '4' or var_op == "D":
            print(f"Operation Selected is : '{var_op}' which is for DIVISION")
            print()
            print(f"DIVISION OF{a} / {b} IS", division(a,b))
            print()
            
        elif var_op == '5' or var_op == "P":
            print(f"Operation Selected is : '{var_op}' which is for PERCENTAGE")
            print()
            print(f"PERCENTAGE OF {a} % {b} IS", percentage(a,b))
            print()
            
            re_call_operation(a,b)
            
        elif var_op == '6' or var_op == "E":
            print(f"Operation Selected is : '{var_op}' which is for Exiting")
            print()
            
        else:
            print("Invalid input")
            
    
    except NameError as e:
        print("Error in OPERATION function",e)


def re_call_operation(a,b):
    try:
        re_call = input("Do you want to perform another operation : \n"
                        "Press 'Y' to Continue \n"
                        "Press 'N' to Exit\n").strip().upper()
        if re_call == "YES" or re_call== "Y":
            print()
            select_operation(a,b)
            N
        elif re_call == "NO" or re_call == "N":
            print("Operation Exited")
        else:
            print("Invalid input")
            
    except ValueError as e:
          print("Input cannot be Number",e)
    
        
check_input()
    