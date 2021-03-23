import random

def quickSort(arr):
	n = len(arr)
	if n <= 1:
		return arr
	p = choosepivot(arr)
	partitionedArr, pIndex = partition(p, arr)
	l = quickSort(partitionedArr[0: pIndex])
	r = quickSort(partitionedArr[pIndex + 1: n])
	l.append(p)
	return l + r 

def choosepivot(arr):
	i = random.randrange(0, len(arr), 1)
	return arr[i]

def partition(p, arr):
	arr.insert(0, arr.pop(arr.index(p)))
	i = 1
	for j in range(1, len(arr)):
		if arr[j] < p:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[0], arr[i-1] = arr[i-1], arr[0]
	return arr, i-1

inputArr = list(map(int, input("Enter your Array:\n").split()))
print(quickSort(inputArr))