class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        opp={"+","-","/","*"}
        def evaluate(a,b,opp):
            if opp=="+":
                return str(a+b)
            if opp=="-":
                return str(a-b)
            if opp=="/":
                temp=a/b
                return str(int(temp))
            if opp=="*":
                return str(a*b)
        stack=[]
        
        for val in tokens:  
            if val in opp:
                right=int(stack.pop())
                left=int(stack.pop())
                stack.append(evaluate(left,right,val))
            else:
                stack.append(val)
        return int(stack.pop())
                
        