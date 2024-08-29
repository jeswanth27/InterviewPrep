
list1=[1,5,3,4,10,9,8]
list2=[1,2,3,4]

for i in range(len(list2)-1):
    if list2[i] < list2[i + 1]:
        k=1
        continue
    else:
        k = 0
        break

if k != 0:
    print("array sorted")
else:
	print("not sorted")