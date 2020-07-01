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
Again this is based on "There will always be only one" rule. Because we can only have one valid answer in the end this is basically at its core a test for is the count odd?

##### FIRST
we need a place to put the ```answer```, so I am going to add it to the dictionary.
```
count_found = {
    "answer": None
}
```
now all we do is test if the count value is odd or not. I tend to use ```%``` to test for remainders my self
```
if count_found[x]%2 == 0:
        #print("even")
        pass
    else:
        #print("odd")
        pass
        count_found["answer"] = x
```
but any odd even logic will do.


### STEP 5) return the result
And now just need to ```return count_found["answer"]``` which should hold the one final odd count value.


****OPS, looks like a use case whole in this logic, in that the order can create a false positive... so we need to fix that to only have the one and only odd


??? Tryy using an [] like a push in pop out list to remove false odds as they are proven even
YEP THAT WORKS, do doc for this...

test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
