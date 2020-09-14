# Fib function
def f(n):

    def helper(n):
        left = f(n-1)
        right = f(n-2)
        return left, right

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        left, right, = helper(n)
        return left + right
