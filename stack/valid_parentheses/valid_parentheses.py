class  ValidParentheses:
    def __init__(self):
        pass
    
    # time = O(n)
    # space = O(n)
    def m1(self, string):
        
        stack = []
        hashMap = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for x in string:
            if x in hashMap:
                if stack[-1] is not hashMap[x] or len(stack) == 0:
                    return false
                else: stack.pop()
            else:
                stack.append(x)

        if len(stack) == 0: return True
        return False

