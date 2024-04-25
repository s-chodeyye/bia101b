def containsDuplicate(nums):
    # solution code here
    for index1 in range(0, len(nums)):
        for index2 in range(0, len(nums)):
            if index1 == index2:
                continue
            print('i1:', index1)
            print('i2:', index2)
            value1 = nums[index1]
            value2 = nums[index2]
            print('value1:', value1)
            print('value2:', value2)
            print('==============')
            if value1 == value2: # Duplicate found
                return True
    
    return False
    # either return True or False