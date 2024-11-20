class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_sign = 1
        result = 0

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += current_sign * current_number
                current_sign = 1
                current_number = 0
            elif char == '-':
                result += current_sign * current_number
                current_sign = -1
                current_number = 0
            elif char == '(':
                stack.append(result)
                stack.append(current_sign)
                result = 0
                current_sign = 1
            elif char == ')':
                result += current_sign * current_number
                result *= stack.pop()
                result += stack.pop()
                current_number = 0

        result += current_sign * current_number
        return result
