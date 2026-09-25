import sys
input = sys.stdin.readline

N = int(input())
users = []

for i in range(N):
    # age, name = map(input().split()) -> 틀림
    age, name = input().split()
    users.append([int(age), name])

for age, name in sorted(users):
    print(age, name)

'''
[문제] 백준 10814 / 링크
[유형] 정렬
[자료구조/알고리즘] 
[시간복잡도] O(N log N)
    - 입력 O(N), 정렬 O(N log N), 출력 O(N)
[처음 생각] 
    
    for age, name in sorted(users):
        print(age, name)
    
[막힌 점/틀린 이유] 
    sorted(users) -> 파이썬은 리스트를 비교할 때 첫 번째 값이 같으면 두 번째 값까지 비교해서 정렬.
    -> 나이가 같으면 이름 알파벳순으로 정렬
    -> ⭐ 정렬 기준(key)을 나이만으로 지정해야 함.
        ** sorted(users, key=lambda x: x[0]) **
[핵심] 
[다음에 조심] 
[다시 풀 날짜] 
'''
