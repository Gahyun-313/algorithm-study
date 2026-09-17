x = int(input("총 금액 x: ")) # 영수증에 적힌 총 금액
y = int(input("종류의 수 y: ")) # 영수증에 적힌 구매한 물건의 종류의 수

sum = 0

for _ in range(y):
    a, b = map(int, input().split())
    sum += a*b

if (sum == x):
    print("Yes")
else:
    print("No")