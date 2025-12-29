A = [5, 3, 2, 4, 1]

A.sort()
print("sort() 결과:", A)

A = [5, 3, 2, 4, 1]
B = sorted(A)
print("원본 리스트:", A)
print("sorted() 결과:", B)

A = [5, 3, 2, 4, 1]
A.sort(reverse=True)
print("내림차순 결과:", A)

B = sorted(A, reverse=True)
print("내림차순 복사본:",B)

A = [5, 3, 2, 4, 1]
A = [-x for x in A]
A.sort()
A = [-x for x in A]

print("부호 반전 방식 내림차순:", A)
