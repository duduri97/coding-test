n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n: # 답을 찾을때
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n: # 현재 합이 답보다 클때
        sum -= start_index
        start_index += 1
    else: # 현재 합이 답보다 작을 때 
        end_index += 1
        sum += end_index

print(count)