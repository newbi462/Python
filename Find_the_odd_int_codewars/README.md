# [Find the odd int](https://www.codewars.com/kata/54da5a58ea159efa38000836)

## The challenge
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

### STEP 0
As always plan what we need to do, in the case we start with:
```
def find_it(seq):
    return None
```
so ```seq``` is our ```list``` or array, which we can verify with ```print(seq)```
```
1) look at all the integer
2) is this a new or old integer
3) keep count of how many found
4) if the count is odd set integer to the result
*Based on "There will always be only one" rule
5) return the result
```


*** use a dict key value set to do this in ONE PASS
