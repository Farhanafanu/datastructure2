#bubble sort
def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
array=[98,5,78,2,43,1]
print("before sort",array)
print("after sort",bubblesort(array))
# def insertionsort(arry):
#     for i in range(len(array)):
#         j=i
#         while array[j-1]>array[j] and j>0:
#             array[j-1],array[j]=array[j],array[j-1]
#             j-=1
#     return array
# array=[98,5,78,2,43,1]
# print("before sort",array)
# print("after sort",insertionsort(array))
# def selectionsort(array):
#     for i in range(len(array)):
#         min=i
#         for j in range(i+1,len(array)):
#             if array[j]<array[min]:
#                 min=j
#         array[i],array[min]=array[min],array[i]
#     return array
# array=[98,5,78,2,43,1]
# print("before sort",array)
# print("after sort",selectionsort(array))
#quicksort
# def partition(array,low,high):
#     pivot=array[low]
#     i=low+1
#     j=high
#     while True:
#         while i<=j and array[i]<=pivot:
#             i+=1
#         while i<=j and array[j]>=pivot:
#             j-=1
#         if i<=j:
#             array[i],array[j]=array[j],array[i]
#         else:
#             break
#     array[low],array[j]=array[j],array[low]
#     return j
# def quicksort(array,low,high):
#     if low<high:
#         pivotindex=partition(array,low,high)
#         quicksort(array,low,pivotindex-1)
#         quicksort(array,pivotindex+1,high)
# array=[98,5,78,2,43,1]
# print("before sorting quick",array)
# quicksort(array,0,len(array)-1)
# print("after sortig",array)
#mergesort
def mergesort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=array[:mid]
    right=array[mid:]
    left=mergesort(left)
    right=mergesort(right)
    return merge(left,right)
def merge(left,right):
    merged=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    while i<len(left):
        merged.append(left[i])
        i+=1
    while j<len(right):
        merged.append(right[j])
        j+=1
    return merged
array=[98,5,78,2,43,1]
print("before sorting ",array)
print("after merge sort",mergesort(array))
