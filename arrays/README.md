###Important Questions from GFG & their patterns

#general approach

#don's use `maxint` as it is not valid
`max_so_far = -maxint - 1 ## maxint returns the lowest value, doing this manipulation helps us handle things
currSum = 0; #Sum that will be updated on each traversal, current case
maxSum = -1e8; #Sum that will be the best case and updated only when currSum > maxSum`