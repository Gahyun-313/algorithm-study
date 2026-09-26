import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# S = list   // 이 문자열이 집합에 있는가?만 확인하면 되므로 list보다 set이 적합
S = set()
count = 0

for _ in range(N):
    # S.append(input().rstrip()) 
    # set에는 append()가 없음. 대신 add() 사용. 
    # list는 순서가 있으므로 "덧붙인다(append)"가 가능. set은 순서가 없으므로 "추가한다(add)"
    S.add(input().rstrip())

for _ in range(M):
    word = input().rstrip()
    if (word in S):
        count += 1

print(count)

'''
[문제] 백준 14425 / 링크
[유형] 해시
[자료구조/알고리즘] set (존재 여부 확인, in 연산자)
[시간복잡도] O(N + M)
    집합 S 받는 데에 O(N), M개 검사하는 데 각각 평균 O(1)이라서 O(M)
[처음 생각] 
    S = list()로 시작 -> word in S 방식으로 확인하려 함
    
[막힌 점/틀린 이유] 
    1) list는 순서가 있어 append, set은 순서가 없어 add를 씀. S.append()를 쓰면 에러
    2) list.count()나 word in list(리스트)는 O(N)이라 N,M이 크면 O(N*M)로 시간 초과 위험
        -> set으로 바꿔서 O(N+M)로 개선
[핵심] 
    "개수"가 아니라 "있는지 없는지"만 필요하면 set이 정답. list로 in을 쓰면 O(N)씩 걸려서 전체 O(N*M)이 됨
[다음에 조심] 
[다시 풀 날짜] 
'''
