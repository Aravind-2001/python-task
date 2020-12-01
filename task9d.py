num_list = [4,9,16,25,18,36,27,49,56]
result = list(filter(lambda x : (x % 9 == 0),num_list))
print("number divisible by 9 are :",result)
