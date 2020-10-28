# if character in word appears once replace with "(" if more then replace with ")". Not case-sensitive.
def duplicate_encode(word):
    i=0
    word = word.lower()
    after = ""
    while i < len(word):
        count = 0
        for x in word:
            if word[i] == x:
                count += 1
                print(count)
        if count > 1:
            after += ")"
            print("rep")
        elif count == 1:
            after += "("
            print("no rep")
        i+=1
    print(after)
    return after