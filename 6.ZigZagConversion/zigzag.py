"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
"""



# SOlution is to traverse the string going down and up between two boundaries which are
# dictated by the numRows contant

# Every time when we reach the boundary, we change the direction

def solution(s, numRows) :
	if numRows == 1 or len(s) < numRows :
		return s

	direction = 1
	row = 1
	lines = dict()

	for char in s :
		if row not in lines :
			lines[row] = char
		else :
			lines[row] += char

		row += direction

		# change direction if we reached either of the ends
		if row == 1 or row == numRows :
			direction *= -1

	return ''.join(lines.values())

if __name__ == "__main__":
	print(solution("paypalishiring", 4))
