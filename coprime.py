def rec_fib(x):
    if x>0:
        return rec_fib(x-1)+rec_fib(x-2)
    else:
        return 1
say=int(input("how many times fibonacci: "))
for i in range(say):
    if i==say-1:
        print(rec_fib(i-1))
    else:
        print(rec_fib(i-1),end=",")
"""1,1,2,3,5,8,13,21,34,55,89"""