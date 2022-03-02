# 피보나치 수열은 첫째와 둘쨰 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열로 Fn = Fn-1 + Fn+2
def fib(n) :
    if n < 2 :
        return 1
    return fib(n-1) + fib(n-2)


print(fib(35)) # Out : 14930352