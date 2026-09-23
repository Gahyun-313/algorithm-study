import sys

input = sys.stdin.readline

arr = list(input().rstrip().split())

print(len(arr))

'''
[문제] 백준 1152
[유형] 
[자료구조/알고리즘] 
[시간복잡도] O(N)
    문자열 input
[처음 생각] 
    split(" ")으로 했는데 -> 단어 사이에 공백이 여러 개 있을 경우 문자 개수를 잘못 세게 됨.
    split() -> 공백을 기준으로 나눔(스페이스, 탭, 줄바꿈 등 모든 공백 문자)
[막힌 점/틀린 이유] 
[핵심] 
[다음에 조심] 
    split()으로 풀기
[다시 풀 날짜] 
'''
