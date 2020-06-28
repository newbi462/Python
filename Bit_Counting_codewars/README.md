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
Thankfully all we need to do here is convert the integer to its binary from with ```bin(n)``` for now for readability I will set it to a var called ```as_binary```


### STEP 2) find our 1s
Python is pretty flexible when it comes to dealing with data so we can loop over pretty much anything with out any work. So following our plan we will loop over each digest if the binary value and look for our ones.
```
for x in as_binary:
    if x is "1":
        print(x)
```
And now we can find all the 1s.
