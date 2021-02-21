def mergeSort(inArr):
	n = len(inArr)
	if n == 1:
		return inArr
	firstHalf = mergeSort(inArr[:n//2])
	secondHalf = mergeSort(inArr[n//2:])
	return merge(firstHalf, secondHalf)

def merge(arr1, arr2):
	i = 0
	j = 0
	k = 0
	result = []
	while k < len(arr1) + len(arr2) and i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j] or j >= len(arr2):
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1
		k += 1
	if i >= len(arr1):
		result.extend(arr2[j:])
	if j >= len(arr2):
		result.extend(arr1[i:])
	return result

def getInput():
    inputArr = list(map(int, input("Enter your Array:\n").split(",")))
    return inputArr

print(mergeSort(getInput()))