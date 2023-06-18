# O(nLog(n)) Time | O(Log(n)) space 
def quicksort(array):
    quickSortHelpler(array,0,len(array)-1)
    return array

def quickSortHelpler(array,startIdx,endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx +=1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -=1
    swap(pivotIdx,rightIdx,array)
    leftSubarrayIsSmaller = rightIdx -1 - startIdx < endIdx -(rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelpler(array,startIdx,rightIdx-1)
        quickSortHelpler(array,rightIdx+1,endIdx)
    else:
        quickSortHelpler(array,rightIdx+1,endIdx)
        quickSortHelpler(array,startIdx,rightIdx-1)

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]



# ................................................................................................................................
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end

def quick_sort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
