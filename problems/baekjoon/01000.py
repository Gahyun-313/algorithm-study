print("1번")
A, B = input().split()
print(int(A) + int(B))  # 숫자 "1"+"2" -> 3
print(A+B)              # 문자열 "1"+"2" -> "12"

print("2번")
A, B = map(int, input().split())
print(A + B) # 숫자 "1"+"2" -> 3