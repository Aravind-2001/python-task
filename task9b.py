from functools import reduce
fib_series=lambda n : reduce(lambda x,_:x+[x[-1]+x[-2]],
                             range(0,2),[0,1])
print("fibonacci series upto 5:")
print (fib_series(5))
