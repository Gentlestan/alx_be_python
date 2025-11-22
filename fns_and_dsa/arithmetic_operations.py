def perform_operation(num1: float, num2: float, operation: "str"):
    
    #Addition
    if operation == "add":
        return num1 + num2
    
    #Subtraction
    elif operation == "subtract":
        return num1 - num2
    
    #multiplication
    elif operation == "multiplication":
        return num1 * num2
    
    #division
    elif operation == "division":
        if num2 == 0:
            return "division by zero"
        return num1 / num2
    
    else:"return invalid operations"
            
        
         
    
    
    
    