import re
reslut = re.finditer(r"([0-9]{1,3})","numbers 23,34,45,56 and 67 ")
print("number of length 1 to 3")
for n in reslut:
    print(n.group(0))
