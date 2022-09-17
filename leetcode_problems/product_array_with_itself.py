def Solution(nums):
    res = []
    for i, a in enumerate(nums):
        product = 1
        for j, b in enumerate(nums):
                if i != j:
                    product *= b;
                                    
        res.append(product)
    
    return res


print(Solution([-1,1,0,-3,3]))