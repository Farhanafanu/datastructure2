def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
array=[8,7,3,6,1,10]
print("before sorting",array)
print("after sorting",bubblesort(array))
#O(n2)