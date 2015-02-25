def caesar_encrypt(str, n):
	result=""
	for s in str:
		bCapital = False
		numLetter = ord(s)
		
		if numLetter >= ord('A') and numLetter <= ord('Z'):
			bCapital = True
			
		n = n % 26
		numShifted = ord(s) + n
		resultLetter = chr(numShifted)
				
		if ( bCapital and numShifted > ord('Z')) or ( not bCapital and numShifted > ord('z')):
			numShifted =  numShifted - 26 
			resultLetter = chr( numShifted )
		
		result = result + resultLetter 
	return result


print caesar_encrypt("ABCZabcz",38)
