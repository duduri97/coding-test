import sys

n = sys.stdin.readline().strip()

# 변수선언
mylist = list(map(int, sys.stdin.readline().strip().split()))

mymax = max(mylist)
mysum = sum(mylist)

print(mysum*100/mymax/int(n))