def Solution2(string):
        stack = []
        markers = [" "] * len(string)
        
        for i, char in enumerate(string):
                if char == "(":
                        stack.append(i)
                elif char == ")":
                        if len(stack) > 0:
                                stack.pop()
                        else:
                                markers[i] = "?"
        
        while len(stack) > 0:
                markers[stack.pop()] = "x"
        
        return f'{string}\n{''.join(markers)}'

lst = ["bge)))))))))", "((IIII))))))", "()()()()(uuu", "))))UUUU((()"]

for i in lst:
        print(Solution2(i))
