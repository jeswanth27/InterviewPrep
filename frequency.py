#frequency of each word
import string

list_values="abbbbccddddeee"
input_set=set(list_values)
print(input_set)
l={}
for i in input_set:
    l[i]=list_values.count(i)

for i in l.keys():
    print(f"keys {i} and value {l.get(i)}")
