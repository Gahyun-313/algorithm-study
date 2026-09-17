n = int(input())
sum = 0

"""
range(시작, 끝, 간격) 
- 끝은 포함하지 않음 (ex. range(1, 5) -> 1, 2, 3, 4)
- 간격은 정수만 가능
"""

for i in range(1, n+1):
    sum += i

print(sum)