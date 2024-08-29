def findmaxnumber(a)->int:
    max=a[0]
    for i in range(1,len(a)):
            if a[i]>max:
                max=a[i]
    return max
if __name__=="__main__":
    lst=[]
    a=input("enter list of elements")
    for i in a.split(" "):
        lst.append(i)

    val=findmaxnumber(lst)
    print(val)
