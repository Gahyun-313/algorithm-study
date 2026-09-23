import sys

input = sys.stdin.readline

N = int(input())
arr = list((input().rstrip())) # 문자
sum_result = 0

# 이렇게 쓸 수도 있음
print(sum(int(i) for i in arr))

for i in arr:
    sum_result += int(i)

print(sum_result)

'''
[문제] 백준 11720 / 링크
[유형] 구현 / 문자열
[자료구조/알고리즘] 리스트(문자열 -> 리스트 변환), 완전 탐색
[시간복잡도] O(N)
    input(O(N)) + for(O(N))
[처음 생각]
    arr를 문자열로 받아서 각 문자가 독립적이게 저장하고
    이를 int로 변환해 합산
[막힌 점/틀린 이유] 
[핵심] 
    ⭐ list("문자열")을 하면 한 글자씩 쪼개져서 리스트의 원소가 됨.
    각 원소는 여전히 문자(str)라서 int()로 변환해야 더할 수 있음.
[다음에 조심] 
[다시 풀 날짜] 
'''
