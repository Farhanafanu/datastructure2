def partition(array,low,high):
    pivot=array[low]
    i=low+1
    j=high
    while True:
        while i<=j and array[i]<=pivot:
            i+=1
        while i<=j and array[j]>=pivot:
            j-=1
        if i<=j:
            array[i],array[j]=array[j],array[i]
        else:
            break
    array[low],array[j]=array[j],array[low]
    return j#pivot index
def quicksort(array,low,high):
    if low<high:
        pivotindex=partition(array,low,high)#pivot index
        quicksort(array,low,pivotindex-1)#leftsublist
        quicksort(array,pivotindex+1,high)#right th sublist
array=[9,4,8,2,7,1,5]
print("before sorting",array)
quicksort(array,0,len(array)-1)
print("after sorting",array)