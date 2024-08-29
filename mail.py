"""
input=jeswanth27@gmail.com
output=j******h27@gmail.com
"""

input_value="jeswanth27@gmail.com"

initial=input_value.split("@")[0]
domain=input_value.split("@")[1]
output=initial[0]+(len(initial[:-2])*'*')+initial[-1]+'@'+domain
print(output)