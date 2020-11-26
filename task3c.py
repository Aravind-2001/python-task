test_key=["ronald","barbie","glory","sam"]
test_value=[9,8,7,6]
print("the key list is:"+str(test_key))
print(" the value list is:"+str(test_value))
res={test_key[i]:test_value[i] for i in range (len(test_key))}
print("resultant dictionary is:"+str(res))
