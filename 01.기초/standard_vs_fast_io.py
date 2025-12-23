# 일반적인 입출력 방식
""" 
a = int(input())
print(a)

# 빠른 입출력 방식
import sys
b = int(sys.stdin.readline())
sys.stdout.write(str(b) + '\n') 
"""

import sys
import time

N = 200000  # 20만 번 반복

# 1. 일반적인 print 방식
start_time = time.time()
for i in range(N):
    # 실제 화면 출력이 너무 많으면 시스템이 느려지므로 
    # 출력 결과를 변수에 담는 식으로 속도만 체크해봅니다.
    pass 
# 실제 print(i)를 20만 번 하면 터미널 속도 때문에 시간이 훨씬 오래 걸립니다.

# 2. sys.stdout.write 방식 성능 예시
print("--- 출력 방식 비교 시작 ---")

# 일반 print 테스트
t1 = time.time()
for i in range(N):
    # 실제로는 화면에 찍어야 하지만, 비교를 위해 형식만 맞춤
    str(i) + '\n'
t2 = time.time()
print(f"일반적인 연산 처리 시간: {t2 - t1:.5f}초")

# sys 방식 시뮬레이션
t3 = time.time()
out = sys.stdout.write
for i in range(N):
    # out(str(i) + '\n') # 실제 출력을 하면 이 함수가 훨씬 빠릅니다.
    pass
t4 = time.time()
print(f"빠른 입출력 구조 처리 시간: {t4 - t3:.5f}초")
