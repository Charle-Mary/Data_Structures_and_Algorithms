class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        all_operators = {"+", "*", "-", "/"}
        current_number, stack, operator = 0, [], "+"

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            if char in all_operators:
                if operator == "+":
                    stack.append(current_number)
                elif operator == "-":
                    stack.append(current_number)
                elif operator == "*":
                    stack[-1] = stack[-1] * current_number
                elif operator == "/":
                    stack[-1] = int(stack[-1] / current_number)

                current_number = 0
                operator = char

        return sum(stack)


