
def sortlist(lst:list) -> list:
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j]>lst[j+1]:
                swap=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=swap

    return lst
if __name__=="__main__":
    list1 = [7,0,9,3,9,6]
    result=sortlist(list1)
    print(result)

