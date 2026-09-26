import sys

input = sys.stdin.readline
# String 입력 -> input().rstrip() 으로 맨 뒤 공백문자 제거

# 가지고 있는 것
N = int(input())
N_cards = list(map(int, input().split()))

# 구분해야 하는 것
M = int(input())
M_num = list(map(int, input().split()))

for i in M_num:
    print(N_cards.count(i), end=" ")

'''
[문제] 백준 10816 / 링크
[유형] 해시 (Counter/dict), 리스트 컴프리헨션
[자료구조/알고리즘] 
[시간복잡도] O( )
    개선 전 : O(N*M) - O(N)인 count()를 M번 반복, 
    개선 후 : O(N+M) - Counter 생성 O(N) 한 번 + 조회 M번(각 O(1))
[처음 생각] 

    for i in M_num:
        print(N_cards.count(i), end=" ")
        
    
[막힌 점/틀린 이유] 
    틀리진 않았지만 시간 복잡도 측면에서 떨어지는 풀이임.
    -> ⭐ set, dict (해시) 사용해서 있는지 확인하는 걸 "세지 않고" 바로 찾는 방법 쓰기
    *"몇 개 있는지 반복해서 세기"보다 "미리 세어서 딕셔너리에 저장해두고 바로 꺼내 쓰기"가 훨씬 빠름.
    
    from collections import Counter
    ~ (동일)
    
    # N_cards를 훑으면서 "각 숫자가 몇 번 나왔는지"를 세서 딕셔너리 형태로 저장
    counts = Counter(N_cards)
    
    # "*" : 리스트를 풀어헤쳐서 각 원소를 별개의 인자로 넘기라는 뜻
    # "[counts[i]] for i in M_num]" : 리스트 컴프리헨션 
    #       -> M_num에 있는 숫자 i를 하나씩 꺼내서 counts에서 그 숫자의 개수를 찾아 새 리스트로 만든다는 뜻
    print(*[counts[i] for i in M_num])
    
[핵심] 
[다음에 조심] 
    N, M이 모두 크게 주어지는 문제에서 리스트의 count()나 in을 반복 호출하면 O(N*M)이 되어 시간 초과 위험. 
    "반복해서 확인해야 하는가?"가 보이면 해시(set/dict/Counter)로 바꿀 수 있는지부터 검토하기
[다시 풀 날짜] 
'''

