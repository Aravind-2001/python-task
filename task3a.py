def Merge(dict1, dict2):
    return(dict2.update(dict1))    
dict1 = {'a': 11, 'b': 12,'c':13}
dict2 = {'d': 14, 'e': 15,'f':16}
print(Merge(dict1, dict2))
print(dict2)
