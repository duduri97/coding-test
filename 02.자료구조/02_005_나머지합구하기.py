import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i] # 합배열 저장하기

for i in range(n):
    reaminder = S[i] % m # 합 배열의 모든 값에 % 연산 수행하기
    if reaminder == 0: # 0~i까지의 구간 합 자체가 0 일때 정답에 더하기
        answer += 1 
    C[reaminder] += 1   # 나머지가 같은 인덱스의 개수 값 증가 시키기

for i in range(m):
    # 나머지가 같은 인덱스중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)

print(answer)