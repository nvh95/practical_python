def bubble_sort2(numbers):
    for i in range(0, len(numbers)):
        for j in range(len(numbers)-1, i-1, -1):
#             print (i,j)
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]

# a = [4,3,2,6,-4, 94,3,2,-1,4,9]
# bubble_sort(a)
# print a