class Solution:
  def calculate(self, s: str) -> int:
    
    # Helper function to perform calculation recursively
    def helper(index):
      stack = []
      num = 0
      sign = "+"

      while index < len(s):
        c = s[index]

        if c.isdigit():
          num = num * 10 + int(c)  # Accumulate the number

        if c == "(":
          # Recursively calculate the value inside the parentheses
          num, index = helper(index + 1)

        # If the current character is an operator or closing parentheses
        if c in "+-*/)" or index == len(s) - 1:
          if sign == "+":
            stack.append(num)
          elif sign == "-":
            stack.append(-num)
          elif sign == "*":
            stack[-1] *= num
          elif sign == "/":
            stack[-1] = int(stack[-1]/num)  # Integer division truncating toward zero

          # Update the sign and reset the number accumulator
          sign = c
          num = 0

          # If closing parenthesis, return the result for this scope
          if c == ")":
            return sum(stack), index

        index += 1

      return sum(stack), index

    result, _ = helper(0)
    return result
