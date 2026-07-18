# Phir .copy() se theek karke dikhao a safe raha.

a = [6,7,8,3]
b = [6,7,8,3]

# the bug:

a=b
b.append(1)
print(b)
print(a)

# solved:

nums = [4,6,7,1]
nums1= nums.copy

nums1=nums.copy()
nums.remove(7)
print(nums)
print(nums1)
