# contains duplicate

* Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

* ex.1
```
Input: nums = [1,2,3,1]
Output: true
```

* ex.2
```
Input: nums = [1,2,3,4]
Output: false
```

* ex.3
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## constraints:
* 1 <= nums.length <= 105
* -109 <= nums[i] <= 109

# solutions

## brute force
```
    loop through all nums
    get index
    loop through all nums again but check with index 
```

## sorting  
```
    sort all nums
    loop through sorted nums 
    check for == next to each other
```

## hash set 
```
    create holder
    loop throygh nums
    if num in holder duplicate
```
