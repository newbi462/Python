def find_it(seq):
    #print(seq)
    #1) look at all the integer
    count_found = {
        "answer": [None]
    }
    def recursion(key_to_check_for):
        try:
            hold = count_found[key_to_check_for]
            #3) keep count of how many found
            count_found[key_to_check_for] += 1
        except KeyError:
            count_found[key_to_check_for] = 1
    for x in seq:
        #print(x)
        #2) is this a new or old integer
        recursion(x)
        #print(count_found)
        #4) if the count is odd set integer to the result
        #print(count_found[x]%2)
        if count_found[x]%2 == 0:
            #print("even")
            #print("len")
            #print(  count_found["answer"][len(count_found["answer"])-1]    )
            #if x == count_found["answer"][len(count_found["answer"])-1]:
            #    count_found["answer"].pop()
            pass
        else:
            #print("odd")
            count_found["answer"].append(x)
    while count_found[count_found["answer"][len(count_found["answer"])-1]]%2 == 0:
        count_found["answer"].pop()



    #5) return the result
    return count_found["answer"][len(count_found["answer"])-1]
