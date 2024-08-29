x=12321
z=0
temp=x
while temp>0:
   y=temp%10
   z=z*10+y
   temp=temp//10
if z==x:
    print("palindrome")
else:
    print("not palindrome")