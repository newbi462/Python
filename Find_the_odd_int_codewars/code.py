def find_it(seq):
    #print(seq)
    #1) look at all the integer
    count_found = {}
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
        print(count_found)


    #4) if the count is odd set integer to the result
    #*Based on "There will always be only one" rule
    #5) return the result
    return None
