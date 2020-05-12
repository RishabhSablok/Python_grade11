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
    def new():
        words = ["a", "b", "c", "d", "e", "f"]
        while len(words) != 0:
            words.pop(0)
        return words
    def new1():
        a = int(input())
        b =[]
        c = 2
        for i in range(a):
            b.append(i + 1)
            
        while c != a+1:
            hh = c/a
            try:
                if float(hh) % 1 == 0:
                    pass
                try:
                    hh = float(hh)
                    hh = int(hh)
                except:
                    pass
            except:
                pass
            if type(hh) == type(4):
                if a % c == 0:
                    return (c)
                    break
            c += 1

"""List_practice.common_end([2],[3])
This is how you call a function from a class"""
print(List_practice.new1())