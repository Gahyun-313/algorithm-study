# Python 코딩테스트 기초 문법과 2주차 자료구조

오랜만에 Python을 사용하는 사람을 위한 학습 노트다. 문법의 의미를 이해하고, 짧은 예제를 실행한 뒤 문제 풀이에 적용하는 순서로 공부한다.

기존 [코딩테스트 로드맵](coding-test-roadmap.md)의 1주차 기초 문법과 2주차 **정렬 / 해시 / 스택 / 큐**에 맞췄다. 정렬은 자료구조가 아니라 데이터를 일정한 기준으로 나열하는 작업이지만, 2주차 학습 범위이므로 함께 다룬다. 힙은 로드맵의 5주차 범위다.

## 목차와 공부 순서

1. [함수와 메서드, 기본 자료형](#1-함수와-메서드-기본-자료형)
2. [입력과 출력: input, split, map, print](#2-입력과-출력-input-split-map-print)
3. [연산자와 조건문](#3-연산자와-조건문)
4. [반복문: range, for, while](#4-반복문-range-for-while)
5. [문자열과 인덱싱, 슬라이싱](#5-문자열과-인덱싱-슬라이싱)
6. [리스트와 튜플](#6-리스트와-튜플)
7. [자주 사용하는 함수와 간결한 문법](#7-자주-사용하는-함수와-간결한-문법)
8. [정렬: sort, sorted, key](#8-정렬-sort-sorted-key)
9. [해시: dict, set, Counter](#9-해시-dict-set-counter)
10. [스택: list](#10-스택-list)
11. [큐: deque](#11-큐-deque)
12. [자료구조 선택과 시간복잡도](#12-자료구조-선택과-시간복잡도)
13. [2주차 학습 계획과 연결](#13-2주차-학습-계획과-연결)
14. [복습 문제](#14-복습-문제)
15. [풀이할 때 옆에 두는 요약표](#15-풀이할-때-옆에-두는-요약표)

처음부터 전부 외울 필요는 없다. 현재 8393번을 푸는 단계에서는 1~4번을 먼저 읽고, 배열·문자열 문제를 풀면서 5~7번을, 2주차에 8~12번을 공부한다. 예제 코드 블록은 원칙적으로 각각 독립적으로 실행한다. 일부러 오류를 설명하는 줄은 주석으로 표시했다.

## 1. 함수와 메서드, 기본 자료형

### 함수와 메서드의 차이

함수는 이름 뒤에 괄호를 붙여 호출한다. 괄호 안에 전달하는 값을 인수라고 한다.

```python
print("hello")   # 화면에 출력하는 함수
print(len("abc"))  # 길이를 구하는 함수 → 3
```

메서드는 특정 값에 연결된 기능이다. `값.메서드()`처럼 점을 붙여 호출한다.

```python
text = "10 20"
print(text.split())  # 문자열의 split 메서드 → ['10', '20']
```

`input()`은 함수이고, `split()`은 문자열의 메서드다. 메서드가 원래 값을 바꾸는지, 새 값을 반환하는지는 메서드마다 다르다.

### 변수와 자료형

```python
count = 3            # int: 정수
average = 2.5        # float: 실수
name = "Python"      # str: 문자열
is_empty = False     # bool: 참 또는 거짓
result = None        # 아직 결과가 없다는 등의 의미로 사용하는 값
```

`=`는 오른쪽 값을 왼쪽 이름에 저장하는 대입 연산자다. 같음을 비교할 때는 `==`를 쓴다.

| 변환 | 결과 | 주의점 |
|---|---|---|
| `int("12")` | 정수 `12` | `int("3.5")`는 오류 |
| `float("3.5")` | 실수 `3.5` | 실수 계산에는 오차가 생길 수 있음 |
| `str(12)` | 문자열 `"12"` | 숫자를 문자열로 변환 |
| `list("abc")` | `['a', 'b', 'c']` | 문자열을 한 글자씩 나눔 |

`sum`, `list`, `str`, `max` 등 기존 함수 이름은 변수 이름으로 피한다. 예를 들어 합계 변수에는 `total`을 사용한다.

## 2. 입력과 출력: input, split, map, print

### input(): 한 줄을 문자열로 입력받기

```python
text = input()   # 123을 입력하면 문자열 "123"
print(type(text))  # <class 'str'>
```

`input()`은 줄 끝의 개행 문자를 제거하지만, 앞뒤 공백을 모두 제거하지는 않는다. 정수 계산이 필요하면 변환한다.

```python
n = int(input())  # 입력: 5
print(n + 1)      # 출력: 6
```

### split(): 문자열 나누기

```python
text = "10 20 30"
parts = text.split()
print(parts)  # ['10', '20', '30']
```

결과는 **문자열을 담은 리스트**다. 숫자처럼 생겨도 아직 정수가 아니다.

구분자를 생략하면 연속된 공백·탭 등의 공백 문자를 기준으로 나누고, 앞뒤 공백으로 빈 항목을 만들지 않는다.

```python
print("  a   b  ".split())    # ['a', 'b']
print("a  b".split(" "))     # ['a', '', 'b']
print("a,b,c".split(","))    # ['a', 'b', 'c']
print("".split())            # []
```

공백으로 구분되는 숫자 입력에는 보통 `.split()`을 사용한다. `.split(" ")`은 연속 공백 사이에 빈 문자열을 만들 수 있다.

### map(): 각 값에 같은 함수 적용하기

```python
parts = ["10", "20", "30"]
numbers = list(map(int, parts))
print(numbers)  # [10, 20, 30]
```

`map(int, parts)`는 `parts`의 각 값에 `int()`를 적용한다. 결과는 리스트가 아니라 차례로 꺼내 쓰는 **이터레이터**다. 리스트로 보관하려면 `list()`로 감싼다.

```python
converted = map(int, ["10", "20"])
print(list(converted))  # [10, 20]
print(list(converted))  # []: 이미 모두 꺼내 썼음
```

### 입력 패턴 1: 한 줄에 정수 두 개

```python
a, b = map(int, input().split())  # 입력: 10 20
print(a + b)                     # 출력: 30
```

실행 순서는 다음과 같다.

1. `input()` → `"10 20"`
2. `.split()` → `["10", "20"]`
3. `map(int, ...)` → 각 문자열을 정수로 변환
4. `a, b = ...` → 값을 하나씩 꺼내 `a = 10`, `b = 20`으로 저장

마지막 단계는 **언패킹**이라고 한다. 변수 두 개에 넣는데 값이 한 개이거나 세 개라면 오류가 발생한다.

### 입력 패턴 2: 한 줄의 정수들을 리스트로 저장

```python
numbers = list(map(int, input().split()))  # 입력: 10 20 30
print(numbers)                            # 출력: [10, 20, 30]
```

### 입력 패턴 3: 정수를 여러 줄로 받기

입력 예시:

```text
3
10
20
30
```

```python
n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

print(numbers)  # [10, 20, 30]
```

`_`는 반복 횟수만 필요하고 반복 변수의 값은 사용하지 않을 때 흔히 쓰는 이름이다. 특별한 문법은 아니다.

### 입력 패턴 4: 붙어 있는 숫자 읽기

```python
digits = list(map(int, input()))  # 입력: 12345
print(digits)                    # [1, 2, 3, 4, 5]
```

공백이 없고 한 글자씩 숫자로 바꾸려는 경우다. `list(map(int, "12345".split()))`은 `[12345]`가 되므로 구분한다.

### print(): 출력 형식 지정하기

```python
print(10, 20)             # 10 20
print(10, 20, sep=",")    # 10,20
print("A", end=" ")      # 기본 줄바꿈 대신 공백
print("B")               # 앞 출력과 합쳐 A B

numbers = [1, 2, 3]
print(numbers)           # [1, 2, 3]
print(*numbers)          # 1 2 3
print(*numbers, sep="\n")  # 숫자를 한 줄에 하나씩 출력
```

`*numbers`는 리스트의 값을 풀어 `print()`의 개별 인수로 전달한다. 제출할 때는 문제에서 요구한 값만 출력하고, `"정답은:"` 같은 안내 문구는 붙이지 않는다.

### 입력이 많을 때: sys.stdin.readline

```python
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
```

입력이 많으면 `sys.stdin.readline()`을 사용하는 방법이 있다. `input()`과 달리 줄 끝의 개행 문자가 남을 수 있다.

```python
line = "hello world\n"  # readline()으로 읽은 문자열이라고 가정
print(line.rstrip("\n"))  # 줄 끝의 개행만 제거
print("  hello  \n".strip())  # hello: 양쪽 공백 문자 제거
```

`int()`와 인수 없는 `.split()`은 주변 공백과 개행을 처리할 수 있으므로 숫자 입력에 매번 `.strip()`을 붙일 필요는 없다. 문자열의 공백이 의미 있는 문제에서는 `.strip()`으로 내용을 지우지 않도록 주의한다.

## 3. 연산자와 조건문

### 계산과 비교

| 문법 | 의미 | 예시 결과 |
|---|---|---|
| `+`, `-`, `*` | 더하기, 빼기, 곱하기 | `3 * 2` → `6` |
| `/` | 나누기 | `7 / 2` → `3.5` |
| `//` | 내림 나눗셈 | `7 // 2` → `3`, `-7 // 2` → `-4` |
| `%` | 나머지 | `7 % 2` → `1` |
| `**` | 거듭제곱 | `2 ** 3` → `8` |
| `==`, `!=` | 같다, 다르다 | `3 != 2` → `True` |
| `<`, `<=`, `>`, `>=` | 크기 비교 | `3 >= 3` → `True` |
| `and`, `or`, `not` | 조건 연결, 부정 | `not True` → `False` |

```python
n = 7

if n % 2 == 0:
    print("짝수")
elif n > 5:
    print("5보다 큰 홀수")
else:
    print("5 이하의 홀수")
```

`if / elif / else`에서는 위에서부터 검사해 처음 만족한 분기 하나만 실행한다. `:` 뒤에 속하는 코드는 일반적으로 공백 4칸으로 들여쓴다.

```python
score = 80
if 0 <= score <= 100:
    print("유효한 점수")
```

### 빈 값 검사와 포함 여부

`0`, `None`, 빈 문자열 `""`, 빈 리스트 `[]`, 빈 딕셔너리 `{}`, 빈 집합 `set()` 등은 조건문에서 거짓으로 취급된다.

```python
numbers = []
if not numbers:
    print("비어 있음")

print(2 in [1, 2, 3])      # True
print(4 not in [1, 2, 3])  # True
print("ab" in "abc")      # True
```

## 4. 반복문: range, for, while

### range(): 시작은 포함, 끝은 제외

```python
range(끝)
range(시작, 끝)
range(시작, 끝, 간격)
```

위 블록은 형태를 설명하는 표기다. 실제 코드에는 숫자나 정의한 변수를 넣는다.

| 예시 | 꺼낼 수 있는 값 |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 5)` | `1, 2, 3, 4` |
| `range(1, 6)` | `1, 2, 3, 4, 5` |
| `range(2, 10, 2)` | `2, 4, 6, 8` |
| `range(5, 0, -1)` | `5, 4, 3, 2, 1` |
| `range(5, 1)` | 없음: 기본 간격 `+1`과 방향이 맞지 않음 |

시작의 기본값은 `0`, 간격의 기본값은 `1`이다. 간격은 `0`일 수 없고, 인수에는 정수를 사용한다.

`range(시작, 마지막 + 1)`은 **1씩 증가하며 마지막 정수까지 포함할 때**의 표현이다. 감소할 때는 끝값을 다르게 잡는다.

```python
print(list(range(3, -1, -1)))  # [3, 2, 1, 0]
```

`range`는 리스트도, 한 번 쓰면 소진되는 `map` 이터레이터도 아니다. 범위를 나타내는 객체이며 반복해서 사용할 수 있다. 모든 정수를 리스트로 미리 저장하지 않으므로 반복문에서는 그대로 사용한다.

### for: 값을 하나씩 꺼내 반복

```python
for number in [10, 20, 30]:
    print(number)

for ch in "abc":
    print(ch)
```

리스트나 문자열도 바로 반복할 수 있다. 단순히 값이 필요하다면 굳이 인덱스를 만들지 않아도 된다.

### 백준 8393: 누적하기

```python
n = int(input())
total = 0

for i in range(1, n + 1):
    total += i

print(total)
```

`total += i`는 여기서 `total = total + i`와 같은 의미다. `n = 3`이면 `total`은 `0 → 1 → 3 → 6`으로 변한다. `print(total)`을 반복문 안으로 들여쓰면 중간 합계까지 출력되므로 위치가 중요하다.

### while, break, continue

```python
i = 1
while i <= 3:
    print(i)  # 1, 2, 3을 각각 출력
    i += 1
```

`while`은 조건이 참인 동안 반복한다. 조건을 바꾸는 코드가 없으면 무한 반복이 될 수 있다.

```python
for i in range(1, 6):
    if i == 2:
        continue  # 이번 반복의 나머지를 건너뜀
    if i == 4:
        break     # 현재 반복문을 끝냄
    print(i)      # 1, 3만 출력
```

## 5. 문자열과 인덱싱, 슬라이싱

### 인덱스: 위치로 하나 꺼내기

```python
text = "python"
print(text[0])   # p: 첫 위치는 0
print(text[2])   # t
print(text[-1])  # n: 마지막 값
print(len(text)) # 6
# print(text[6]) # IndexError: 유효한 양수 방향 인덱스는 0~5
```

### 슬라이싱: 일부 구간 꺼내기

`값[시작:끝:간격]` 형태이고 끝 위치는 제외한다.

```python
text = "python"
print(text[1:4])  # yth
print(text[:3])   # pyt
print(text[3:])   # hon
print(text[::2])  # pto
print(text[::-1]) # nohtyp
print(text[:99])  # python: 슬라이싱의 끝이 길이를 넘어도 오류가 아님
```

같은 문법을 리스트와 튜플에도 사용할 수 있다. 문자열은 일부 글자를 직접 바꿀 수 없는 **불변 자료형**이다.

```python
text = "cat"
# text[0] = "b"  # TypeError
text = "b" + text[1:]
print(text)       # bat: 새 문자열을 만들어 변수에 저장
```

### 자주 사용하는 문자열 메서드

| 문법 | 의미 | 결과 |
|---|---|---|
| `"AbC".lower()` | 소문자로 변환 | `"abc"` |
| `"AbC".upper()` | 대문자로 변환 | `"ABC"` |
| `"banana".count("a")` | 등장 횟수 | `3` |
| `"banana".find("na")` | 처음 등장한 위치 | `2` |
| `"banana".find("x")` | 없으면 `-1` | `-1` |
| `"a-b".replace("-", ":")` | 문자열 치환 | `"a:b"` |
| `" ".join(["a", "b"])` | 구분자로 문자열들 연결 | `"a b"` |

문자열 변환 메서드는 원본을 바꾸지 않는다. 결과가 필요하면 반환된 값을 저장한다.

```python
text = "ABC"
lower_text = text.lower()
print(text)        # ABC
print(lower_text)  # abc

numbers = [1, 2, 3]
print(" ".join(map(str, numbers)))  # 1 2 3
```

`join()`에 넘기는 항목은 문자열이어야 한다. 정수 리스트는 `map(str, ...)`로 변환한다.

## 6. 리스트와 튜플

### list: 순서가 있고 수정할 수 있는 값의 모음

```python
numbers = [10, 20, 30]
numbers[0] = 100
numbers.append(40)
print(numbers)  # [100, 20, 30, 40]

last = numbers.pop()
print(last)     # 40: 삭제한 값을 반환
print(numbers)  # [100, 20, 30]
```

| 문법 | 동작 | 주의점 |
|---|---|---|
| `a.append(x)` | 맨 뒤에 값 하나 추가 | 리스트를 넣으면 리스트 자체가 한 항목으로 들어감 |
| `a.extend(values)` | 여러 값을 하나씩 뒤에 추가 | `a.extend([2, 3])` |
| `a.insert(i, x)` | 위치 `i`에 삽입 | 뒤쪽 원소를 이동하므로 느릴 수 있음 |
| `a.pop()` | 마지막 값을 삭제하고 반환 | 비어 있으면 오류 |
| `a.pop(i)` | 위치 `i`의 값을 삭제하고 반환 | 앞쪽 삭제는 뒤의 원소를 이동 |
| `a.remove(x)` | 처음 나온 값 `x` 삭제 | 값이 없으면 오류 |
| `a.count(x)` | 값 `x`의 개수 | 리스트 전체를 훑음 |
| `a.index(x)` | 값 `x`의 첫 인덱스 | 값이 없으면 오류 |

```python
a = [1]
a.append([2, 3])
print(a)  # [1, [2, 3]]

b = [1]
b.extend([2, 3])
print(b)  # [1, 2, 3]
```

`append()`는 리스트를 수정하고 `None`을 반환한다. `a = a.append(2)`처럼 쓰면 `a`가 `None`이 된다.

### 대입과 복사 구분하기

```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)  # [99, 2, 3]: 같은 리스트를 가리킴

c = a.copy()
c[0] = 0
print(a)  # [99, 2, 3]: 바뀌지 않음
```

`copy()`와 `a[:]`는 바깥 리스트만 복사하는 **얕은 복사**다. 내부에 리스트가 있으면 내부 리스트는 공유한다.

### 리스트 컴프리헨션과 2차원 리스트

반복해서 값을 만들어 리스트에 담는 문법이다.

```python
squares = [x * x for x in range(1, 5)]
print(squares)  # [1, 4, 9, 16]

evens = [x for x in range(1, 7) if x % 2 == 0]
print(evens)    # [2, 4, 6]
```

2차원 리스트는 리스트 안에 행별 리스트를 넣은 형태다.

```python
rows, cols = 2, 3
grid = [[0] * cols for _ in range(rows)]
grid[0][1] = 7
print(grid)  # [[0, 7, 0], [0, 0, 0]]
```

다음처럼 만들면 같은 행 리스트를 여러 번 참조하므로 주의한다.

```python
grid = [[0] * 3] * 2
grid[0][1] = 7
print(grid)  # [[0, 7, 0], [0, 7, 0]]: 두 행이 함께 바뀜
```

### tuple: 순서가 있지만 원소를 교체할 수 없는 묶음

```python
point = (3, 5)
x, y = point
print(x, y)  # 3 5
# point[0] = 9  # TypeError

single = (3,)  # 값이 하나인 튜플은 쉼표가 필요
```

좌표 `(x, y)`나 `(나이, 이름)` 같은 묶음을 표현할 때 사용한다. 리스트와 달리 원소 추가·삭제·교체를 할 수 없다. 단, 튜플 안에 리스트가 있다면 그 내부 리스트의 내용까지 불변이 되는 것은 아니다.

## 7. 자주 사용하는 함수와 간결한 문법

### len, sum, min, max, abs

```python
numbers = [3, 1, 4]
print(len(numbers))  # 3: 개수
print(sum(numbers))  # 8: 합계
print(min(numbers))  # 1: 최솟값
print(max(numbers))  # 4: 최댓값
print(abs(-7))       # 7: 절댓값
```

`sum([])`은 `0`이지만, `min([])`과 `max([])`는 기본값을 지정하지 않으면 오류가 난다.

### enumerate: 인덱스와 값을 함께 꺼내기

```python
names = ["민수", "지수"]
for index, name in enumerate(names):
    print(index, name)  # 0 민수 / 1 지수 (각각 한 줄)

for rank, name in enumerate(names, start=1):
    print(rank, name)   # 1 민수 / 2 지수 (각각 한 줄)
```

### zip: 여러 묶음에서 하나씩 짝짓기

```python
names = ["민수", "지수"]
scores = [80, 90]
for name, score in zip(names, scores):
    print(name, score)
```

기본적으로 더 짧은 쪽의 길이만큼만 반복한다.

### 함수 정의와 반환

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

`print()`는 화면에 출력하고, `return`은 호출한 곳에 결과를 돌려주면서 함수를 끝낸다. 명시적인 반환값이 없는 함수는 `None`을 반환한다.

### f-string: 문자열에 값 넣기

```python
name = "Python"
count = 3
print(f"{name} 문제를 {count}개 풀었다.")
```

## 8. 정렬: sort, sorted, key

### sort와 sorted의 차이

```python
numbers = [3, 1, 2]
new_numbers = sorted(numbers)
print(numbers)      # [3, 1, 2]: 원본 유지
print(new_numbers)  # [1, 2, 3]: 새 리스트

result = numbers.sort()
print(numbers)      # [1, 2, 3]: 원본 변경
print(result)       # None
```

| 문법 | 원본 변경 | 반환값 |
|---|---|---|
| `a.sort()` | 리스트 자체 변경 | `None` |
| `sorted(a)` | 원본 유지 | 정렬된 새 리스트 |
| `sorted(a, reverse=True)` | 원본 유지 | 내림차순 새 리스트 |

`a = a.sort()`는 흔한 실수다. 원본을 정렬하려면 `a.sort()`만 호출한다. `sorted()`는 리스트뿐 아니라 문자열·튜플·집합 등 반복 가능한 값도 받을 수 있고, 결과는 리스트다.

### key와 lambda: 무엇을 기준으로 정렬할지 지정

```python
words = ["pear", "a", "cat"]
print(sorted(words, key=len))  # ['a', 'cat', 'pear']
```

`key`에 전달한 함수가 각 항목에서 정렬 기준값을 계산한다. 항목 자체가 길이로 바뀌는 것은 아니다.

```python
students = [(21, "민수"), (20, "지수"), (21, "영희")]
students.sort(key=lambda student: student[0])
print(students)  # [(20, '지수'), (21, '민수'), (21, '영희')]
```

`lambda student: student[0]`은 입력받은 항목의 첫 번째 값을 돌려주는 짧은 함수다. 다음 함수를 만들어 `key=age_of`로 전달하는 것과 같은 기준이다.

```python
def age_of(student):
    return student[0]
```

Python 정렬은 **안정 정렬**이다. 기준값이 같으면 원래 입력 순서를 유지한다. 나이순 정렬에서 같은 나이의 가입 순서를 유지해야 할 때 활용한다.

### 기준이 여러 개인 정렬

```python
points = [(2, 1), (1, 3), (1, 2)]
print(sorted(points))  # [(1, 2), (1, 3), (2, 1)]
```

튜플은 앞 원소부터 비교한다. 첫 값이 같으면 다음 값을 비교하므로 좌표의 x 오름차순, 같으면 y 오름차순 정렬에 사용할 수 있다.

```python
records = [(80, "B"), (90, "C"), (90, "A")]
print(sorted(records, key=lambda item: (-item[0], item[1])))
# [(90, 'A'), (90, 'C'), (80, 'B')]
```

위 예제는 점수 내림차순, 같은 점수에서는 이름 오름차순이다. `reverse=True`는 전체 기준의 방향을 뒤집으므로 서로 다른 방향을 지정할 때는 기준별로 표현한다.

숫자 문자열은 정수와 정렬 결과가 다를 수 있다.

```python
print(sorted(["10", "2", "1"]))  # ['1', '10', '2']
print(sorted([10, 2, 1]))        # [1, 2, 10]
```

## 9. 해시: dict, set, Counter

해시는 값에서 계산한 정보를 이용해 저장 위치를 찾는 방식이다. Python에서는 딕셔너리와 집합을 통해 활용한다. 처음에는 직접 해시 함수를 구현하기보다 **이름으로 값을 찾을지, 존재 여부만 확인할지, 개수를 셀지**를 구분한다.

### dict: 키로 값을 찾기

```python
scores = {"민수": 80, "지수": 90}
print(scores["민수"])       # 80
scores["민수"] = 85         # 기존 값 변경
scores["영희"] = 95         # 새 키 추가
print("민수" in scores)     # True: 키가 있는지 검사
print(scores.get("철수", 0))  # 0: 없을 때 사용할 기본값
# print(scores["철수"])     # KeyError
```

같은 키를 다시 저장하면 이전 값이 바뀐다. `in`은 값이 아니라 **키**를 검사한다. `.get(key, 기본값)`은 키가 없어도 기본값을 반환할 뿐, 새 항목을 추가하지 않는다.

```python
scores = {"민수": 80, "지수": 90}
for name, score in scores.items():
    print(name, score)

print(list(scores.keys()))    # ['민수', '지수']
print(list(scores.values()))  # [80, 90]
del scores["민수"]            # 키와 값을 삭제
```

딕셔너리는 삽입 순서를 유지하지만, 키가 자동으로 정렬되는 것은 아니다.

### dict로 등장 횟수 세기

```python
numbers = [3, 1, 3, 2, 1, 3]
counts = {}

for number in numbers:
    counts[number] = counts.get(number, 0) + 1

print(counts)            # {3: 3, 1: 2, 2: 1}
print(counts.get(9, 0))  # 0
```

처음 나온 숫자는 기존 개수를 `0`으로 보고 `1`을 더한다. 이미 나온 숫자는 저장해 둔 개수를 증가시킨다.

### set: 중복 없이 저장하고 존재 여부 확인

```python
seen = set()  # 빈 집합. {}는 빈 딕셔너리이므로 구분
seen.add("apple")
seen.add("apple")
seen.add("banana")

print(len(seen))          # 2
print("apple" in seen)    # True
seen.discard("orange")   # 없어도 오류 없음
# seen.remove("orange")  # 없으면 KeyError
```

집합은 인덱스로 접근할 수 없고 순서를 보장하지 않는다. 집합을 출력한 순서에 의존해서는 안 된다.

```python
a = {1, 2, 3}
b = {3, 4}
print(sorted(a | b))  # [1, 2, 3, 4]: 합집합
print(sorted(a & b))  # [3]: 교집합
print(sorted(a - b))  # [1, 2]: 차집합
```

`set(numbers)`는 중복을 제거하지만 등장 횟수도 사라진다. 횟수가 필요한 문제는 딕셔너리나 `Counter`를 사용한다.

### dict 키와 set 원소의 제한

키와 집합 원소는 **해시 가능한 값**이어야 한다. 정수·문자열·정수로 구성된 튜플은 사용할 수 있지만, 리스트·딕셔너리·집합 자체는 사용할 수 없다.

```python
visited = {(1, 2), (3, 4)}
print((1, 2) in visited)  # True
# visited.add([5, 6])     # TypeError: 리스트는 해시 불가능
```

튜플도 내부 원소가 모두 해시 가능해야 한다. 리스트를 포함한 튜플은 키로 사용할 수 없다.

### Counter: 개수 세기를 간단하게

```python
from collections import Counter

counts = Counter([3, 1, 3, 2, 1, 3])
print(counts[3])  # 3
print(counts[9])  # 0: 없는 항목 조회도 가능
print(Counter("banana")["a"])  # 3
```

문자별 등장 횟수가 같은지도 비교할 수 있다.

```python
from collections import Counter

print(Counter("listen") == Counter("silent"))  # True
```

`collections`는 Python 표준 라이브러리이므로 별도 설치 없이 `import`해서 사용한다.

## 10. 스택: list

스택은 **나중에 넣은 것을 먼저 꺼내는 구조(LIFO)**다. 접시를 쌓았다가 위에서부터 꺼내는 순서와 같다.

Python에서는 리스트의 **뒤쪽**을 입구와 출구로 사용한다.

```python
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack[-1])  # 30: 확인만 함
print(stack.pop())  # 30: 꺼내면서 삭제
print(stack.pop())  # 20
print(stack)        # [10]
```

| 동작 | Python 코드 |
|---|---|
| 넣기 | `stack.append(x)` |
| 꺼내기 | `stack.pop()` |
| 가장 위 값 확인 | `stack[-1]` |
| 크기 확인 | `len(stack)` |
| 비어 있는지 확인 | `not stack` |

빈 스택에서 `pop()`이나 `[-1]`을 사용하면 오류가 난다.

```python
stack = []
if stack:
    print(stack.pop())
else:
    print(-1)
```

### 적용 예시: 괄호 짝 맞추기

```python
def is_valid_parentheses(text):
    stack = []

    for ch in text:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()

    return not stack

print(is_valid_parentheses("(())"))  # True
print(is_valid_parentheses("())"))   # False
print(is_valid_parentheses("(("))    # False
```

이 예제는 입력이 `(`와 `)`로만 구성된다고 가정한다. 닫는 괄호를 만날 때 가장 최근의 여는 괄호를 제거한다. 중간에 짝이 없거나, 끝난 뒤 여는 괄호가 남으면 실패다.

## 11. 큐: deque

큐는 **먼저 넣은 것을 먼저 꺼내는 구조(FIFO)**다. 줄을 선 사람이 먼저 온 순서대로 나가는 것과 같다.

```python
from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)

print(queue[0])        # 10: 앞의 값 확인
print(queue[-1])       # 30: 뒤의 값 확인
print(queue.popleft()) # 10: 앞에서 꺼내면서 삭제
print(list(queue))     # [20, 30]
```

`deque`는 양쪽 끝에서 추가·삭제할 수 있는 자료구조다. 일반적인 큐는 오른쪽으로 넣고 왼쪽에서 꺼내는 방식으로 사용한다.

| 동작 | Python 코드 |
|---|---|
| 오른쪽에 넣기 | `queue.append(x)` |
| 왼쪽에서 꺼내기 | `queue.popleft()` |
| 왼쪽에 넣기 | `queue.appendleft(x)` |
| 오른쪽에서 꺼내기 | `queue.pop()` |
| 비어 있는지 확인 | `not queue` |

빈 큐에서 꺼내거나 양 끝 값을 조회하면 오류가 나므로 먼저 확인한다.

### 큐에 list.pop(0)을 반복해서 쓰지 않는 이유

리스트의 첫 값을 삭제하면 나머지 값들의 위치를 앞으로 옮겨야 한다. 길이가 N인 리스트에서 `pop(0)`은 O(N)이지만, `deque.popleft()`는 O(1)이다.

```python
from collections import deque

queue = deque([1, 2, 3])
while queue:
    current = queue.popleft()
    print(current)  # 1, 2, 3을 각각 출력
```

### 적용 예시: 맨 앞의 값을 맨 뒤로 옮기기

```python
from collections import deque

queue = deque([1, 2, 3, 4])
queue.append(queue.popleft())
print(list(queue))  # [2, 3, 4, 1]
```

카드나 대기 순서를 순환시키는 문제에 사용할 수 있다. 이 한 줄도 큐가 비어 있지 않을 때만 실행해야 한다.

## 12. 자료구조 선택과 시간복잡도

### 문제에서 필요한 동작으로 고르기

| 필요한 동작 | 우선 고려할 도구 | 예시 |
|---|---|---|
| 순서대로 저장하고 인덱스로 접근 | `list` | 점수 목록 |
| 좌표처럼 값을 묶기 | `tuple` | `(x, y)` |
| 이름이나 번호로 연결된 값 찾기 | `dict` | 이름별 점수 |
| 중복 제거, 존재 여부 확인 | `set` | 등록된 문자열 조회 |
| 값별 등장 횟수 세기 | `dict`, `Counter` | 숫자 카드 개수 |
| 가장 최근에 넣은 값부터 꺼내기 | `list`를 스택으로 사용 | 괄호 검사 |
| 먼저 넣은 값부터 꺼내기 | `deque`를 큐로 사용 | 대기열 처리 |
| 값의 크기나 특정 기준으로 나열 | `sort`, `sorted` | 나이순·좌표순 정렬 |

### O(1), O(N), O(N log N)의 의미

N은 저장한 값의 개수다. 시간복잡도는 정확한 실행 시간을 초 단위로 뜻하는 것이 아니라, 데이터가 늘 때 필요한 작업량이 어떻게 늘어나는지 나타낸다.

- **O(1)**: 개수가 늘어도 대략 일정한 작업량. 예: 리스트의 특정 인덱스 조회.
- **O(N)**: 전체를 한 번 훑는 정도. 예: 리스트에서 값 검색.
- **O(N log N)**: 일반적인 효율적인 비교 정렬의 규모.
- **O(N²)**: 각 원소마다 전체 원소를 다시 훑는 정도. N이 크면 부담이 빠르게 커진다.

| 연산 | 일반적인 시간복잡도 | 주의점 |
|---|---|---|
| `len(list)`, `len(dict)`, `len(set)`, `len(deque)` | O(1) | 크기 조회 |
| `list[i]` | O(1) | 위치로 접근 |
| `x in list`, `list.count(x)` | O(N) | 순서대로 확인 |
| `list.append(x)` | 분할 상환 O(1) | 여러 번 실행한 전체 비용을 나눈 기준 |
| `list.pop()` | O(1) | 맨 뒤 삭제 |
| `list.pop(0)`, 앞쪽 삽입·삭제 | O(N) | 원소 이동 필요 |
| `dict[key]`, `key in dict`, `x in set` | 평균 O(1) | 최악에는 O(N) 가능 |
| 딕셔너리·집합의 추가·삭제 | 평균 O(1) | 해시 충돌 등에 영향받음 |
| `deque.append`, `deque.popleft` 등 양 끝 추가·삭제 | O(1) | 큐에 적합 |
| `deque[0]`, `deque[-1]` | O(1) | 양 끝 조회 |
| deque 중간 인덱스 조회, `x in deque` | O(N) | 임의 위치 접근에는 리스트가 유리 |
| `sorted`, `list.sort` | 최악 O(N log N) | 정렬 기준 비교 비용이 일정하다고 가정 |

정수처럼 비교·해시 계산 비용을 작게 볼 수 있는 값을 기준으로 정리한 표다. 긴 문자열이나 복잡한 `key` 함수에서는 해당 계산 비용도 고려한다.

예를 들어 N개의 카드에 대해 M번 개수를 묻는데 매번 `cards.count(x)`를 쓰면 O(NM)이다. `Counter`로 먼저 개수를 세면 일반적인 해시 성능을 가정할 때 준비 O(N), M번 조회 O(M)으로 전체 평균 O(N + M)이 된다.

## 13. 2주차 학습 계획과 연결

아래는 기존 로드맵의 문제 중 해당 문법을 연습하기 좋은 연결점이다. 전체 문제 목록은 [로드맵](coding-test-roadmap.md)을 확인한다.

| 일정 | 먼저 읽을 내용 | 연결 문제 | 스스로 설명할 내용 |
|---|---|---|---|
| Day 1: 정렬 | 리스트, `sort`, `sorted`, 슬라이싱 | 백준 2750, 2751 / 프로그래머스 K번째수 | 원본을 바꿀지, 정렬한 새 리스트를 만들지 |
| Day 2: 정렬 기준 | 튜플, `key`, `lambda`, 안정 정렬 | 백준 10814, 11650 | 기준이 같은 값의 순서를 어떻게 처리할지 |
| Day 3: 해시 | `dict`, `get`, `set`, `Counter` | 백준 10816, 14425 / 완주하지 못한 선수 | 존재 여부와 등장 횟수 중 무엇이 필요한지 |
| Day 4: 스택 | `append`, `pop`, 빈 값 검사 | 백준 10828, 9012 | 가장 최근 값을 먼저 처리해야 하는 이유 |
| Day 5: 큐 | `deque`, `popleft` | 백준 10845, 2164, 1966 | 가장 먼저 들어온 값을 먼저 처리하는 방법 |

각 항목은 **설명 읽기 → 출력 예상하기 → 직접 실행하기 → 문제에 적용하기** 순서로 공부한다.

## 14. 복습 문제

### A. 실행 결과 예상하기

```python
print(" 10   20 ".split())
print(list(range(5, 0, -2)))
print("python"[1:4])
print(sorted(["10", "2", "1"]))
```

<details>
<summary>정답과 이유</summary>

```text
['10', '20']
[5, 3, 1]
yth
['1', '10', '2']
```

- `split()`은 연속된 공백을 구분자로 처리한다.
- `range(5, 0, -2)`는 5부터 2씩 감소하고 0은 포함하지 않는다.
- 슬라이싱은 인덱스 1부터 4 직전까지다.
- 숫자 문자열은 숫자 크기가 아니라 문자열 순서로 비교한다.

</details>

### B. 입력과 누적 연습

한 줄에 공백으로 구분된 정수들이 주어질 때, 짝수만 더해 출력해 보자.

입력 `1 2 3 4 5 6`의 출력은 `12`다.

<details>
<summary>예시 풀이</summary>

```python
numbers = list(map(int, input().split()))
total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print(total)
```

</details>

### C. 등장 횟수 연습

`[2, 3, 2, 5, 3, 2]`에서 `2`와 `9`의 개수를 각각 구해 보자. 정답은 `3`, `0`이다. 딕셔너리로 먼저 풀고 `Counter`로도 작성해 본다.

<details>
<summary>예시 풀이</summary>

```python
numbers = [2, 3, 2, 5, 3, 2]
counts = {}
for number in numbers:
    counts[number] = counts.get(number, 0) + 1

print(counts.get(2, 0))  # 3
print(counts.get(9, 0))  # 0
```

```python
from collections import Counter

counts = Counter([2, 3, 2, 5, 3, 2])
print(counts[2])  # 3
print(counts[9])  # 0
```

</details>

### D. 스택과 큐 비교

두 자료구조에 `10`, `20`, `30`을 차례로 넣고, 각각 두 번 꺼냈을 때의 결과를 예상해 보자.

<details>
<summary>정답과 확인 코드</summary>

스택은 `30, 20`, 큐는 `10, 20`이다.

```python
from collections import deque

stack = [10, 20, 30]
queue = deque([10, 20, 30])
print(stack.pop(), stack.pop())          # 30 20
print(queue.popleft(), queue.popleft())  # 10 20
```

</details>

## 15. 풀이할 때 옆에 두는 요약표

| 하고 싶은 일 | 문법 |
|---|---|
| 정수 하나 입력 | `n = int(input())` |
| 정수 두 개 입력 | `a, b = map(int, input().split())` |
| 한 줄의 정수들을 리스트로 | `a = list(map(int, input().split()))` |
| 한 글자씩 정수로 | `digits = list(map(int, input()))` |
| N번 반복 | `for _ in range(n):` |
| 1부터 N까지 반복 | `for i in range(1, n + 1):` |
| 인덱스와 값 함께 반복 | `for i, value in enumerate(a):` |
| 합계 / 최솟값 / 최댓값 | `sum(a)` / `min(a)` / `max(a)` |
| 리스트 맨 뒤 추가 / 삭제 | `a.append(x)` / `a.pop()` |
| 원본 정렬 / 새 정렬 리스트 | `a.sort()` / `sorted(a)` |
| 내림차순 정렬 | `sorted(a, reverse=True)` |
| 두 번째 값을 기준으로 정렬 | `sorted(a, key=lambda x: x[1])` |
| 키가 없으면 기본값 | `d.get(key, 0)` |
| 개수 누적 | `d[x] = d.get(x, 0) + 1` |
| 중복 제거 | `set(a)` |
| 포함 여부 확인 | `x in collection` |
| 빈 상태 확인 | `if not collection:` |
| 큐 만들기 | `from collections import deque` 후 `q = deque()` |
| 큐에 넣기 / 꺼내기 | `q.append(x)` / `q.popleft()` |
| 리스트를 공백으로 구분해 출력 | `print(*a)` |

실수 점검: **입력은 문자열인지 정수인지 / 범위의 끝이 제외되는지 / 빈 자료구조인지 / 원본을 바꾸는 메서드인지 / 존재 여부와 개수 중 무엇이 필요한지**를 확인한다.
