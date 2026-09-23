n = int(input())

# 입력을 배열로 받음
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))

"""
// input()이 느려서 시간 초과 나는 문제에서는 이렇게 씀
import sys

input = sys.stdin.readline
n_list = list(map(int, input().split())
"""