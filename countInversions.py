def countInversionsAndSort(inArr):
    n = len(inArr)
    if n == 1:
        return (inArr,0)
    firstHalf = countInversionsAndSort(inArr[:n//2])
    secondHalf = countInversionsAndSort(inArr[n//2:])
    return countSplitInversionsAndMerge(firstHalf[0], secondHalf[0], firstHalf[1] + secondHalf[1])

def countSplitInversionsAndMerge(arr1, arr2, inversionsCount = 0):
    i = 0
    j = 0
    k = 0
    len1 = len(arr1)
    len2 = len(arr2)
    result = []
    while k < len1 + len2 and i < len1 and j < len2:
        if arr1[i] <= arr2[j] or j >= len2:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
            inversionsCount += len1-i
        k += 1
    if i >= len1:
        result.extend(arr2[j:])
    if j >= len2:
        result.extend(arr1[i:])
    return (result, inversionsCount)

def getInput():
    inputArr = list(map(int, input("Enter your Array:\n").split(",")))
    return inputArr

print(countInversionsAndSort(getInput())[1])