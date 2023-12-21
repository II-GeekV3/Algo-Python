
def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = -1
    if (n == 0):
        fn = f0
    if (n == 1):
        fn = f1
    for k in range(2,n):
        fn = f1 + f0
        f0,f1 = f1,fn
    return fn

print(fibonacci(10))