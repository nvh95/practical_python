def bubble_sort(numbers):
    for i in range(len(numbers),1,-1):
        for j in range(0, i-1):
            #print (i,j)
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

a = [4,3,2,6,-4, 94,3,2,-1,4,9]
bubble_sort(a)
print a