ba = 18228
aa = [22,3,15]

def bonus(arr, s):
    total = 0
    arr2=[]
    for i in arr:
        total += i
    print(total)
    for i in range(0, (len(arr))):
        arr2.append(ba - (s/total * arr[i]))
    print(arr2)
    return(arr2)

bonus(aa,ba)