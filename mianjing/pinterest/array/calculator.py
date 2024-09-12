class Solution:
  def q1(self, expression:str):
  # Initialize variables to hold the current result and operator
    result = 0
    current_operator = None
    i = 0

    while i < len(expression):
        # Check if the current character is a minus sign and handle negative numbers
        is_negative = False
        if expression[i] == '-':
            is_negative = True
            i += 1

        # Extract the number
        num = 0
        while i < len(expression) and expression[i].isdigit():
            num = num * 10 + int(expression[i])
            i += 1

        # Apply negative sign after extract number
        if is_negative:
            num = -num
        
        # If it's the first number, initialize result
        if current_operator is None:
            result = num
        else:
            # Apply the operator
            if current_operator == '+':
                result += num
            elif current_operator == '*':
                result *= num
        
        # Move to the next operator
        if i < len(expression):
            current_operator = expression[i]
            i += 1


    print(result)
    return result
    
sol = Solution()
sol.q1('11+1*2')