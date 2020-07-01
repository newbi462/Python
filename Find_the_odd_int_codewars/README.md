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


****OPS, looks like a use case whole in this logic, in that the order can create a false positive... so we need to fix that to only have the one and only odd.

## The Problem, and the fix
```
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
```
In other words while ```10``` should be the answer ```1``` replaces it because of the order of the list. So how can we fix this?

Well we can use a ```[]``` as a Stack or LIFO (last in first out) so we keep track of all our matches and then remove ones we do not want to keep.
```
count_found = {
    "answer": [None]
}
```
so now we can ```count_found["answer"].append(x)``` any odd counts to this list, and ```count_found["answer"].pop()``` any that become even using
```
while count_found[count_found["answer"][len(count_found["answer"])-1]]%2 == 0:
      count_found["answer"].pop()
```
The result is the order no no longer matters, and ends of this stack that are not an ```odd``` count will be removed until only a true ```odd``` is the last value. And we can return that
```
return count_found["answer"][len(count_found["answer"])-1]
```
This is far from pretty, and the resulting ```code.py``` is full of dead ends, but I will leave them commented out so you can follow along. This solution reduces to
```
def find_it(seq):
    count_found = {
        "answer": [None]
    }
    def recursion(key_to_check_for):
        try:
            hold = count_found[key_to_check_for]
            count_found[key_to_check_for] += 1
        except KeyError:
            count_found[key_to_check_for] = 1
    for x in seq:
        recursion(x)
        if count_found[x]%2 == 0:
            pass
        else:
            count_found["answer"].append(x)
    while count_found[count_found["answer"][len(count_found["answer"])-1]]%2 == 0:
        count_found["answer"].pop()
    return count_found["answer"][len(count_found["answer"])-1]
```
and honestly, it has neither an optimal space or time complexity. But hay, we followed the plan.



Ok, so we had fun with CS and Data Structures, but you know there is ```count()```
```
def find_it(seq):
  for x in seq:
      if seq.count(x)%2!=0:
          return x
```
Just saying...
