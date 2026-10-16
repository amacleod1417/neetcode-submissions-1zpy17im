import math

class Solution:

    def isOp(self, i: str):
        return i == "+" or i == "-" or i == "*" or i == "/"

    def Op(self, one: int, two: int, op: str):

        match op:
            case "+":
                return one + two
            case "-":
                return one - two
            case "*":
                return one * two
            case "/":
                return int(one / two)
            
    
    def evalRPN(self, tokens: List[str]) -> int:
       
        stack = []

        for i in tokens:
            
            if not self.isOp(i): 
                stack.append(int(i))
            
            else:
                two = stack.pop()
                one = stack.pop()
                stack.append(self.Op(one, two, i))
            
        return stack[0]

    


                





    

            


                
