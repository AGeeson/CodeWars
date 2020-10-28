# find the int that appears ana odd amount of times in an array/list 
def find_it(seq):
    odd = 0
    for x in seq:
        if seq.count(x)%2 == 1:
            odd = x
    return odd
