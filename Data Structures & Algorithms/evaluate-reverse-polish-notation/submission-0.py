class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # 先彈出的是右運算元，後彈出的是左運算元
                n2 = stack.pop()
                n1 = stack.pop()
                
                if token == "+":
                    stack.append(n1 + n2)
                elif token == "-":
                    stack.append(n1 - n2)
                elif token == "*":
                    stack.append(n1 * n2)
                elif token == "/":
                    stack.append(int(n1 / n2))
            else:
                # 遇到數字字串，轉成整數後推入堆疊
                stack.append(int(token))
                
        return stack[0]