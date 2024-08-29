
def main():
    print("Hello World!")
    a=list(input("Enter the list of elements to sort"))
    for i in range(len(a)-1):
        for j in range(len(a) - 1 - i):
            if(a[j]>a[j+1]):
                swap=a[j]
                a[j]=a[j+1]
                a[j+1]=swap

    for k in range(len(a)):
        print(a[k])

if __name__== "__main__":
    main()

