#Time Complexity = O(n^2)

l = [10,5,8,20,2,18]

def selectionsort(l):
    n = len(l)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if l[j] < l[min_index]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]
    return l

print(selectionsort(l))