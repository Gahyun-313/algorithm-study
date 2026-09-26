from collections import Counter

def solution(s, t):
    
    # s_set = list(Counter(s.split("")))
    # Counter는 문자열을 바로 넣어도 됨
    
    # ⭐ list로 바꾸지 말고 Counter 객체끼리 그대로 비교!
    
    return print(Counter(s) == Counter(t))

solution("anagram", "nagaram")
solution("rat", "cat")