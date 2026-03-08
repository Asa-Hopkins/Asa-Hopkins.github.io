#Converts a given decimal string to binary
def to_binary(x):
    #Step 1, initialise variables
    s = 0
    d = 0
    #Start on units column
    column_value = 1
    while d < len(x):
        #Read the d'th digit from the right
        digit = x[-1-d]
        
        #Convert the digit value to binary
        digit = ord(digit) - ord('0')
        #Step 2, add digit value to s
        s = s + digit*column_value
        d += 1
        column_value = 10*column_value
    #Make sure the user sees the result in binary
    return bin(s)
    
#Converts a given number to a decimal string
def to_string(x):
    d = 1
    column_value = 10
    #Step 2, find number of digits in result
    while column_value < x:
        d += 1
        column_value *= 10
    output = ""
    while d != 0:
        #Step 4
        d -= 1
        column_value //= 10
        
        #Integer division gives largest multiple
        digit = x//column_value
        output += chr(digit + ord('0'))
        
        #Step 5
        x = x - column_value*digit
    return output
        
