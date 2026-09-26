from collections import Counter

def solution(participant, completion):
    answer = ''
    
    for i in completion:
        if (i in participant):
            
            # "del" -> del a[i] : 인덱스로 삭제
            # "remove" -> a.remove(n) : 일치하는 첫 번째 값을 찾아서 삭제
            # "pop" -> val = a.pop(i) : 인텍스 i번 삭제 후 val에 대입
            participant.remove(i)
    
    answer = participant[0]
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# i in participant, participant.remove(i) -> 둘 다 리스트를 처음부터 끝까지 훑는 동작이라서 각각 O(N)
# 이걸 completion의 원소 개수만큼 반복하니 전체는 O(M * N)
# ✅ 해시로 개선하기
# 이름별로 몇 명이 있는지를 비교해야 하는 문제 -> Counter 사용
# >> 참가자 명단의 이름별 개수 - 완주자 명단의 이름별 개수 = 완주 못한 사람의 이름만 개수 1로 남음
def solution2(participant, completion):
    
    # ["leo", "kiki", "eden"] - ["eden", "kiki"] 와 동일 -> ["leo"]
    temp = Counter(participant) - Counter(completion)
    
    # temp.keys() : 딕셔너리에서 **키만 뽑아서** 돌려주는 메서드
    # -> dict_keys는 인덱싱이 바로 안 되므로 list()로 감싸서 리스트화.
    answer = list(temp.keys())[0]
    return answer

print(solution2(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution2(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

"""
[유형] 해시
[자료구조/알고리즘] Counter (dict 기반), 딕셔너리 뺄셈
[시간복잡도] 
    solution (remove 방식): O(N * M)  - in participant, remove()가 각각 O(N), completion 개수만큼 반복
    solution2 (Counter 방식): O(N + M)  - Counter 생성이 각각 O(N), O(M), 뺄셈도 그 합만큼
[처음 생각] 
    participant 리스트에서 completion에 있는 이름을 하나씩 remove()로 제거 -> 남는 하나가 정답
    
[막힌 점/틀린 이유]
    로직은 맞았지만 in participant + remove()가 각각 O(N)이라 전체 O(N * M). N,M이 최대 10만이라 시간 초과 위험
    -> Counter(participant) - Counter(completion)으로 개선. 뺄셈 결과엔 개수가 남는(양수인) 값만 남음

[핵심] 
    ⭐"이름별 개수를 비교"해야 하는 문제는 Counter끼리 뺄셈이 유용함. 완주 못한 사람은 참가자 수 - 완주자 수가 1로 남아서 자동으로 걸러짐

[다음에 조심] 
    list에 대해 in / remove / count를 반복문 안에서 쓰면 O(N * M)이 되기 쉬움 -> 반복 조회가 필요하면 먼저 해시(set/dict/Counter)로 바꿀 수 있는지 검토
[다시 풀 날짜]
"""
