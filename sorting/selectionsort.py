def selectionsort(array):
    for i in range(len(array)):
        min=i
        for j in range(i+1,len(array)):
            if array[j]<array[min]:
                min=j
        array[i],array[min]=array[min],array[i]
    return array
array=[6,3,8,1,9,2]
print("before sorting",array)
print("after sorting",selectionsort(array))
#O(n2)