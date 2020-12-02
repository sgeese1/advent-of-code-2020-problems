def printTuples(arr, arr_size, sum):  
    s = set() 
    for i in range(0, arr_size-1):  
        temp = sum - arr[i]
        for j in range(i + 1, arr_size):
            if (temp - arr[j]) in s:
                print (arr[i] * arr[j] * (temp-arr[j]))

            s.add(arr[i])

file = open('day1_input.txt', 'r')
array = []
for line in file:
    array.append(int(line))
target_sum = 2020
printTuples(array, len(array), target_sum)