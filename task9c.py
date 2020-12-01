num = [10,23,45,56,67]
n = 45
print("the list:",num)
print("given number:",n)
filtered_numbers=list(map(lambda number:number*n,num))
print("result")
print(''.join(map(str,filtered_numbers)))
