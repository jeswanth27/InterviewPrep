def f_commonalpha(input1:str,input2:str)->list:
    input_set1=set(input1)
    input_set2=set(input2)
    print("common letters",input_set1.intersection(input_set2))
    print("All letters",input_set1.union(input_set2))
    print("Present in first not in second",input_set1.intersection(input_set2))
    print("Present in second not in first", input_set2 - input_set1)
    lst=[]

    for i in input_set1:
        if input_set2.__contains__(i):
            lst.append(i)

    return lst
if __name__=="__main__":
    result_list=f_commonalpha("jeswanth","naidu")
    print(result_list)
