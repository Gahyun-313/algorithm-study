import sys

input = sys.stdin.readline

N = int(input())

arr = set() # set: 중복 허용하지 않는 집합 자료형, 순서 지원x
            # dict.fromkeys(): 원래 리스트의 순서를 유지하면서 중복을 없앰

for i in range(N):
    arr.add(int(input()))

for num in sorted(arr): # 내림차순으로 쓰러면 -> for num in sorted(arr, reverse=True)
    print(num)

'''
[문제] 백준 2750 / 링크
[유형] 정렬
[자료구조/알고리즘] set(중복 제거), sorted() 정렬
[시간복잡도] O(N log N). 입력 받는 건 O(N), 정렬 자체가 O(N log N).
[처음 생각] 
    arr = set()
    for i in range(N): arr.add(int(input()))
    print(arr.sort()) -> 여기서 틀림
[막힌 점/틀린 이유] 
    sort()는 리스트에만 있는 메서드인데 set에 사용해서 틀림. (set에는 순서가 없으므로 정렬도 불가)
    set으로 중복 제거 한 후 리스트로 바꿔서 정렬하면 됨. 
        -> sorted() 사용. set을 정렬해서 새 리스트로 돌려줌. (arr 자체는 안 바뀜)
        
    ** list.sort()는 반환하지 않고 그 자리에서 정렬만 함(print(list.sort()) -> none이 됨)
[핵심] 
    sort()는 리스트를 그 자리에서 바로 정렬(반환값 없음), 
    sorted()는 원본은 그대로 두고 정렬된 새 리스트를 반환. set에는 sort()가 없음
[다음에 조심] 
[다시 풀 날짜] 
'''
