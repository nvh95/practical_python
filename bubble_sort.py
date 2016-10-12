def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

# a = [4,3,2,6,-4, 94,3,2,-1,4,9]
# bubble_sort(a)
# print a