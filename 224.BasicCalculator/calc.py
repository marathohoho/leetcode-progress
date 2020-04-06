'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

def calc(s) :
	res = 0
	operand = 0
	sign = 1
	stack = []

	for c in s :
		if c.isdigit():
			operand = (operand * 10) + int(c)
		elif c == '+' :
			res += sign * operand
			sign = 1
			operand = 0
		elif c == '-' :
			res += sign * operand
			sign = -1
			operand = 0
		elif c == '(' :
			stack.append(res)
			stack.append(sign)

			res = 0
			sign = 1
		elif c == ')' :
			res += sign * operand
			res *= stack.pop()
			res += stack.pop()

			operand = 0
	return res + operand * sign`



