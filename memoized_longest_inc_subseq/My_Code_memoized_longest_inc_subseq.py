# 모르겠다.. 예제 코드 보고 공부하자

# 동적 계획법으로 풀 수 있는 유명한 알고리즘 문제이다.
# 어떤 임의의 수열이 주어질 때, 이 수열에서 몇 개의 수들을 제거해서 부분수열을 만들 수 있다.
# 이때 만들어진 부분수열 중 오름차순으로 정렬된 가장 긴 수열을 최장 증가 부분 수열이라 한다.
"""
ex)
3 5 7 9 2 1 4 8

3 7 9 1 4 8 (5, 2 제거)
7 9 1 8 (3, 5, 2, 4 제거)
3 5 7 8 (9, 2, 1, 4 제거)
1 4 8 (3, 5, 7, 9, 2 제거)
"""

# from benchmark import benchmark
# from functools import wraps
#
# def memo(func) :
#     cache = {}
#
#     @wraps(func)
#     def wrap(*args) :
#         if args not in cache :
#             cache[args] = func(*args)
#         return cache[args]
#     return wrap()
#
# @wraps
# def memoized_longest_inc_subseq(seq) :


s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]
print(memoized_longest_inc_subseq(s1))

