import sys

input = sys.stdin.readline

for i in range(int(input())): # 0 ~ T-1
    string = input().rstrip()
    print(string[0] + string[-1])

'''
[문제] 백준 9086 / 링크
[유형] 구현 / 문자열
[자료구조/알고리즘] 문자열 인덱싱 (string[0], string[-1])
[시간복잡도] O(N)
[처음 생각] 
    """
	input = sys.stdin.readline.rstrip()
	for i in range(int(input())):
    """
        -> 라고 했다가 for문에서 에러남.
[막힌 점/틀린 이유] 
	sys.stdin.readline : 함수 자체(아직 호출되지x)
    .rstrip() : 문자열에 사용하는 메서드
    -> input.rstrip() : input은 함수 자체라서 .rstrip()을 붙일 대상이 없음 -> 에러
    -> input().rstrip() : input()으로 먼저 문자열을 붙이고 그 문자열에 .rstrip()을 붙이는 것이므로 맞음
[핵심] 
	숫자 input은 rstrip() 사용x
	rstrip 사용 시 input().rstrip()으로 사용
[다음에 조심] 
[다시 풀 날짜] 
'''
