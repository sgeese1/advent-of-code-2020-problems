def printPairs(arr, arr_size, sum):
     
    s = set()
     
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in s):
            print (arr[i] * temp)
        s.add(arr[i])

file = open('day1_input.txt', 'r')
array = []
for line in file:
    array.append(int(line))
target_sum = 2020
printPairs(array, len(array), target_sum)

