def countBits(n):
    #print(n)
    #1) convert the number to the binary we need to check and add up
    as_binary = bin(n)
    #print(as_binary)
    #2) find our 1s
    result = 0
    for x in as_binary:
        if x is "1":
            #print(x)
            #3) add them to our answer
            result += 1
    return result 
