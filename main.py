# nums = [0,1,2,3,4]
# indeks = [0,1,2,2,1]
#
# empty = []
# [empty.insert(indeks[i], nums[i]) for i in range(len(indeks))]
# print(empty)

# 3065. Минимальные операции, превышающие пороговое значение I
# nums = [2,11,10,1,3]
# k = 10
# print(len([num for num in nums if num < k]))

# 1528 - Shuffle-string

# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# d = {}
# for i in range(len(s)):
#     d[indices[i]] = s[i]
# print(''.join([i[1] for i in sorted(d.items(), key=lambda x: x[0])]))


# 2341 - Maximum amount of pairs in array


# 2108 - Find first palindromic string in array
# s = ["abc","car","ada","racecar","cool"]
# for i in s:
#     if i == i[::-1]:
#         return i
# else:
#     return ''



# 1684 - Count  the number of consistent strings
# allowed = "ab"
# words = ["ad", "bd", "aaab", "baa", "badab"]
# words = ["a","b","c","ab","ac","bc","abc"]
# print(sum(1 for word in words if set(word).issubset(allowed)))



# 3158 - Find the XOR of numbers that appear twice
# import functools
# from operator import xor
#
# nums = [1, 2, 3]
# result = []
# for num in nums:
#     if nums.count(num) == 2 and num not in result:
#         result.append(num)
# print(functools.reduce(xor, (0, )))


#  1313
# nums = [1,2,3,4]
# result = [2,4,4,4]
# s = ''
# for i in range(1, len(nums), 2):
#     s += f'{nums[i]} '*nums[i - 1]
# print(list(map(int, s.split())))




# 3162

# nums1 = [1,3,4]
# nums2 = [1,3,4]
# k = 1

# nums1 = [1,2,4,12]
# nums2 = [2,4]
# k = 3

# c = 0
# for j in nums2:
#     for i in nums1:
#         if i % (j*k) == 0:
#             c += 1
# print(c)


# MATRIXXXXXXXXXXXXXXXXXXXX

# grid = [
#     [9,9,8,1],
#     [5,6,2,6],
#     [8,2,6,4],
#     [6,2,2,2]
# ]
# result =  [
#     [9,9],
#     [8,6]
# ]
# res = []
# for i in range(1, len(grid) - 1):
#     for j in range(1, len(grid) - 1):
#         print(grid[i][j], end=' ')
#     print()


# grid[1][1]
# grid[1][1 - 1]
# grid[1 - 1][1 - 1]
# grid[1 - 1][1]
# grid[1 - 1][1 + 1]
# grid[1][1 + 1]
# grid[1 + 1][1 + 1]
# grid[1 + 1][1 - 1]
from functools import reduce
from itertools import combinations
from operator import xor

nums = [5,1,6]
result = 6

# print(list(combinations(nums, r=2)))

# c = 0
# for i in range(2, len(nums) + 1):
#     for j in list(combinations(nums, r=i)):
#         c += reduce(xor, j)
# return c + sum(nums)





#  Design

l = ['']*2
print()