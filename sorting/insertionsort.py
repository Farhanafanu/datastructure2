def insertionsort(array):
    for i in range(len(array)):
        j=i
        while array[j-1]>array[j] and j>0:
            array[j-1],array[j]=array[j],array[j-1]
            j-=1
    return array
array=[4,7,1,9,2,10]
print("element before sorting",array)
print("element after sorting",insertionsort(array))
#O(n2)