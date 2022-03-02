from benchmark import benchmark
from functools import wraps


def memo(func):
    cache = {}

    @wraps(func) # @ : Decorator를 한마디로 얘기하자면, 대상 함수를 Wrapping 하고, Wrapping 된 함수의 앞뒤에 추가적으로 꾸며질 구문들을 정의해서 손쉽게 재사용 가능하게 해주는 것입니다.
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@memo
def fib2(n):
    if n < 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


def fib3(m, n):
    if m[n] == 0:
        m[n] = fib3(m, n-1) + fib3(m, n-2)
    return m[n]


@benchmark
def check_fib(n):
    print(fib(n))


@benchmark
def check_fib2(n):
    print(fib2(n))


@benchmark
def check_fib3(n):
    m = [0] * (n+1)
    m[0], m[1] = 1, 1
    print(fib3(m, n))


if __name__ == "__main__":
    n = 35
    check_fib(n)
    check_fib2(n)
    check_fib3(n)
