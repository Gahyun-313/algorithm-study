import sys

input = sys.stdin.readline

N = int(input())

arr = set()

for i in range(N):
    arr.add(int(input()))

for num in sorted(arr):
    print(num)
'''
[문제] 백준 2751 / 링크
[유형] 정렬
[자료구조/알고리즘] 
[시간복잡도] O(N log N)
    - 정렬은 N log N
[처음 생각] 
[막힌 점/틀린 이유] 
[핵심] 
[다음에 조심] 
[다시 풀 날짜] 
'''
