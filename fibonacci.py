
def fibnocci_series(n) -> list:
    fib_series=[0,1,1]
    for i in range(3,n):
        next_num=fib_series[-1]+fib_series[-2]+fib_series[-3]
        fib_series.append(next_num)

    return fib_series[:n]


if __name__=="__main__":
    result=fibnocci_series(5)
    print(result)


