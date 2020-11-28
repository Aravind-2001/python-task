num = int(input("enter a number:"))
sum_= 0
temp = num
while temp > 0:
   digit = temp % 10
   sum_ += digit ** 3
   temp //= 10
if num == sum_:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
