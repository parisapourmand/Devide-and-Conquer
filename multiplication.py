def multiplyStrings(str1, str2):
	if len(str1) == 1 or len(str2) == 1:
		return multiplyStringByChar(str1, str2)
	else:
		result = "0"
		for i in range(len(str2)):
			result = addStrings(multiplyStringByChar(str1, str2[-i-1]) + ['0']*i, result)
	return result

def multiplyStringByChar(inStr, ch):
	overflow = '0'
	result = []
	for i in range(len(inStr)):
		multiOut = addStrings(multiplyChars(inStr[-i-1], ch), overflow)
		result.insert(-i-1, multiOut[-1])
		if len(multiOut) > 1:
			overflow = multiOut[-2]
		else:
			overflow = '0'
	result.insert(0, overflow)
	return result

def multiplyChars(ch1, ch2):
	num1 = int(ch1)
	num2 = int(ch2)
	return str(num1*num2)

def addStrings(str1, str2):
	n1 = len(str1)
	n2 = len(str2)
	if n1 >= n2:
		n = n1
		for i in range(n1 - n2):
			str2 = "0" + str2
	else:
		n = n2
		for i in range(n2 - n1):
			str1 = "0" + str1
	overflow = '0'
	result = []
	for i in range(n):
		tempResult = str(int(str1[-i - 1]) + int(str2[-i - 1]) + int(overflow))
		result.insert(-i - 1, tempResult[-1])
		if len(tempResult) > 1:
			overflow = tempResult[-2]
		else:
			overflow = '0'
	result.insert(0, overflow)
	return result

first = input("Enter the first number: ")
second = input("Enter the second number: ")
print(int(''.join(multiplyStrings(first,second))))