# [Bit Counting](https://www.codewars.com/kata/526571aae218b8ee490006f4)

## The challenge
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of ```1234``` is ```10011010010```, so the function should return ```5``` in this case.

### STEP 0
As always plan what we need to do, in the case we start with:
```
def countBits(n):
```
so ```n``` is our ```1234```, which we can verify with ```print(n)```

```
1) convert the number to the binary we need to check and add up
2) find our 1s
3) add them to our answer
```

### STEP 1) convert the number to the binary we need to check and add up
Thankfully all we need to do here is convert the integer to its binary form with ```bin(n)``` for now for readability I will set it to a var called ```as_binary```.


### STEP 2) find our 1s
Python is pretty flexible when it comes to dealing with data so we can loop over pretty much anything without any work. So following our plan we will loop over each digest of the binary value and look for our ones.
```
for x in as_binary:
    if x is "1":
        print(x)
```
And now we can find all the 1s.

### STEP 3) add them to our answer
Well we have the ones, but that is not what we wanted to know; we want to know how many of them we have. So let us make a ```result``` var to return and ```+1``` it each time we find a ```1```.

### STEP 4) ???
Ok, we got the result we want but never said to actually ```return``` it, so we should probably do that.
```
return result
```

### Less is more?
Now, rather this final code with all these comments in ```code.py``` is or is not a mess honestly depends on the in house style guidelines.

If you are a fan of fewer comments and fewer lines you could condense this to:
```
def countBits(n):
    result = 0
    for x in bin(n):
        if x is "1":
            result += 1
    return result
```
But, this is one of those subjective points of readability.
