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
### STEP 1) look at all the integer
Thankfully Python will let us loop over almost any thing so
```
for x in seq:
      print(x)
```
will give us our individual list values to look at.

### STEP 2) is this a new or old integer
This is where data structures and some basic CS will let us make a more efficient one pass solution.

##### FIRST
We need a key value set, in the case of Pyhton a dictionary will do for this very primitive ```key/values``` hash table
```
count_found = {}
```
##### NEXT
we can use ```except KeyError:``` to test ```is this a new or old integer```
```
try:
    hold = count_found[key_to_check_for]
except KeyError:
    count_found[key_to_check_for] = 1
```
And to contain the scope of this error will will use recursion to contain it to a ```recursion(x)``` function.

### STEP 3) keep count of how many found
We now have a list of values as we find them but we are not keeping track of how many we found. so lets add that
```
count_found[key_to_check_for] += 1
```
to increment our count in the ```recursion(key_to_check_for)``` we made in the last step

### STEP 4) if the count is odd set integer to the result
Again this is based on "There will always be only one" rule.

### STEP 5) return the result

*** use a dict key value set to do this in ONE PASS
