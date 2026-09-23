import sys

#input = sys.stdin.readline
word = input()
print(len(word))

'''
[문제] 백준 2743
[유형] 구현 / 문자열
[자료구조/알고리즘] 문자열(str), len() 내장함수
[시간복잡도] O(N) : N은 문자열 길이. 
    입력을 읽는 데 O(N), 
    len()은 파이썬이 문자열 길이를 따로 저장해두기 때문에 그 자체는 O(1)
[처음 생각] 
    input = sys.stdin.readline 으로 받아서 len()으로 글자 수 읽기
[막힌 점/틀린 이유] 
    input()은 줄 끝의 개행문자(\n)를 자동으로 제거해주지만,
    readline()은 개행문자까지 그대로 읽기 때문에 +1됨.
    
[핵심] 
    짧은 문자는 input()으로 읽으면 되지만,
    입력이 많아서 readline()을 쓸 때는 **.rstrip()**을 붙인다. -> word = sys.stdin.readline().rstrip()
[다음에 조심] 
[다시 풀 날짜] 
'''
