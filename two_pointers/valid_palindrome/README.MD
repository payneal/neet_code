# Valid Palidrome
* A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

* Given a string s, return true if it is a palindrome, or false otherwise.

 

## Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

## Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

## Example 3:
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

# Constraints:
```
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
```

# Solutions:
* time = O(n)
* space = O(1
```
# create pointer for l and r
    
    # while L < R 

        # while l < r and string[l] is alnum
            # move l pointer

        # while l < r and string[r] is alnum
            # move r pointer

        # check if pointer values == if ! return False 

        # move pointers 1 spot
    
    # is true 


```
