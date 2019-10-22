import datetime
import sys
from functools import reduce
#
# a = '''
# int("13", base=6)
# '''
# print(eval(a))

# def f(x,y):
#     return x+y
# print(reduce(f,range(1,11)))


# def datetimeFormat(func):
#     print(func(0,0))
#     def wrap(*args, **kwargs):
#         print(args[0])
#         return func(*args,**kwargs)
#     return wrap
#
# @datetimeFormat
# def day_period(enddate,period,*args,**kwargs):
#     pass

a = [3,3]
b =6
def twosum(nums,target):
    aa = [(i,target-i) for i in [i for i in nums if i<target] if target-i in [i for i in nums if i<target] and target-i!= i]
    for i in aa:
        return [nums.index(i[0]),nums.index(i[1])]
print(twosum(a, b))


def twosum1(nums,target):

    aa = [(i,target-i) for i in [i for i in nums if i<target] if target-i in [i for i in nums if i<target] and target-i!= i]
    for i in aa:
        return [nums.index(i[0]),nums.index(i[1])]
print(twosum(a, b))


# a = Dior空山基超限定白色机械裸女樱花短袖tee 请注意图案  全球限定300件 超级补货一件 SIZE M 国内现货秒发 特价好货可得5800 调货价格5180
# b = Dior空山基超限定白色机械裸女樱花短袖tee 请注意图案  全球限定300件 超级补货一件 SIZE M 国内现货秒发 特价好货可得5800 调货价格5180
# print(a==b)



#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in [(i,target-i) for i in [i for i in nums if i<target] if target-i in [i for i in nums if i<target]]:
#             return [nums.index(i[0]),nums.index(i[1])]
#
#
#
#
# Solution.twoSum()















