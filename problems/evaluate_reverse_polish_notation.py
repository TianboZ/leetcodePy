from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
                print(stack)
            elif item == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
                print(stack)
            elif item == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
                print(stack)
            elif item == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append( int(n2/n1))
                print(stack)
            else:
                # e.g. -10, 10
                num = int(item)
                stack.append(num)
        
        print(stack)
        if stack:
            return stack[0]
        return 0