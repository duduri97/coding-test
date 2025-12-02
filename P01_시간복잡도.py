N = 100000
cnt = 1

# 연산 횟수 = N
# for i in range(N):
#     print("연산 횟수 " + str(cnt))
#     cnt += 1

# 연산 횟수 = N²
for i in range(N):
    for j in range(N):
        print("연산 횟수 " + str(cnt))
        cnt += 1

