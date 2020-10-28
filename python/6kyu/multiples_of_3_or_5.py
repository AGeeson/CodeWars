# sum or multiples of 3 or 5 below input number. eg: input 10 - > output 23
def solution(number):
    i = 0
    total = 0
    while i < number:
        if i%3 == 0 or i%5 == 0:
            total += i
            print(total)
        i+=1
    return total

