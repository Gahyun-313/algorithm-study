import sys

input = sys.stdin.readline

N, x = map(int, input().split())
a = list(map(int, input().split()))

for v in a: # 0 ~ n-1 -> n번
    if (v < x):
        print(v, end=" ")
        
'''
[문제] 백준 10871 : x보다 작은 수
[유형] 구현(배열 순회)
[자료구조/알고리즘] 리스트, 완전탐색 (모든 원소를 한 번씩 확인)
[시간복잡도] O(N) : for문 1개로 원소를 한 번씩만 확인
[처음 생각] 
[막힌 점/틀린 이유] 
    - list에 input() 받는 방법을 몰랐음 : list(map(int, input().split()))
    - x보다 크거나 같은 요소를 a[]에서 삭제하려고 했음. 처음에 a의 길이를 알려줬다는 걸 까먹음
        - list 삭제: del a[i], a.remove(값), val = a.pop(i)
        - 위의 삭제 방식은 지운 뒤 뒤에 있는 원소들을 한 칸씩 당김 -> 한 번에 O(N)이 걸림
        이를 for문 안에서 반복할 경우 O(N^2)에 걸릴 수 있음
        - 순회하는 리스트에서 원소를 지우면 인덱스가 밀려서 원소를 건너뛰는 버그도 생김
[핵심] 
    - 원소를 지우지 말고 **조건에 맞는 것만 골라서 출력** 
[다음에 조심] 
[다시 풀 날짜] 
'''
