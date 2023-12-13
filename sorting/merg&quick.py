#quick sort
# def partition(array,low,high):
#     pivot=array[low]
#     i=low+1
#     j=high
#     while True:
#         while i<=j and array[i]<=pivot:
#             i+=1
#         while i<=j and array[j]>pivot:
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
# array=[4,2,6,1,98,30,3]
# print("element before sorting",array)
# quicksort(array,0,len(array)-1)
# print("after sorting",array)
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
array=[4,2,6,1,98,30,3]
print("elemnet before sorting",array)
print("element after sorting",mergesort(array))