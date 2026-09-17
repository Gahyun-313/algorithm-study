# 커밋 메시지 컨벤션

일반적인 `feat`/`fix`/`docs` 컨벤션은 문제 풀이 저장소와 잘 맞지 않아서,
아래 규칙을 사용한다.

## 기본 형식

```
<type>(<플랫폼>): <번호/난이도> - <문제명>
```

## type 목록

- `solve`    : 새 문제 풀이 커밋
- `resolve`  : 이미 푼 문제를 다른 방식으로 재풀이
- `note`     : 오답노트만 추가/수정
- `refactor` : 기존 풀이 코드 리팩터링 (로직 변경 없음)
- `chore`    : 로드맵/템플릿/구조 등 저장소 관리용 변경

## 플랫폼별 예시

- `solve(baekjoon): 2557 - Hello World`
- `solve(baekjoon): 10869 - 사칙연산`
- `solve(programmers): lv1 - 완주하지 못한 선수`
- `solve(leetcode): 242 - Valid Anagram`
- `solve(softeer): lv2 - 장애물 인식 프로그램`

## 여러 문제를 한 커밋으로 묶을 때

```
solve(baekjoon): 2557, 10869 - Day1 입출력/구현
```

## 오답노트만 추가할 때

```
note(baekjoon): 1697 - 오답노트 추가 (BFS 큐 조건 실수)
```

## 재풀이할 때

```
resolve(baekjoon): 1697 - 숨바꼭질 (반복 BFS로 재풀이)
```

## 본문 (선택)

필요하면 제목 아래에 시간복잡도/공간복잡도, 다시 풀 날짜를 한 줄로 남긴다.

```
solve(baekjoon): 2178 - 미로 탐색

시간복잡도: O(N*M), 공간복잡도: O(N*M)
```
