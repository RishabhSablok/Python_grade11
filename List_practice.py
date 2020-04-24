class List_practice():
    # Practice Question number 1 (first_last6)
    def first_last6(nums):
        #nums = str(input("Input the items: "))
        num_list = list(map(int, nums.split()))
        if num_list[0] == 6 or num_list[-1] == 6:
            return True
        else:
            return False 
    def common_end(a, b):
        if a[0] == b [0] or a[len(a)-1] == b[len(b)-1]:
            return True
        else:
            return False
    def reverse3(nums):
        a = nums[0] 
        nums[0] = nums[2]
        nums[2] = a
        return nums
    def middle_way(a, b):
        c = [a[1], b[1]]
        return c
    def same_first_last(nums):
        if nums[0] == nums[len(nums)-1]:
            return True
        else:
            return False

"""List_practice.common_end([2],[3])
This is how you call a function from a class"""