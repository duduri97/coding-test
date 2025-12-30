# import sys

# N = sys.stdin.readline()
# input_list = []
# result = 0

# for i in N:
#     input_list[i] = sys.stdin.readline()

# for i in N:
#     result += input_list[i] 

# print(result)


import sys
n = int(sys.stdin.readline())
sum = 0

numbers = list(sys.stdin.readline().strip())

for i in range(n):
    sum += int(numbers[i])

print(sum)
