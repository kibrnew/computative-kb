class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        def turn(i,j):
            if i%j==0:
                return i//j
            else:
                if i/j > 0:
                    return i//j 
                else:
                    return (i//j +1)
        for i in range(len(tokens)):
            x=tokens[i]
            if x=="+":
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append(str(a+b))
            elif x=="-":
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append( str(a-b))
            elif x=="*":
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append( str(a*b))
            elif x=="/":
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append( str(turn(a,b)))
            else: 
                stack.append(x)
        return int(stack[0])

