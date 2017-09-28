#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:41:32 2017

@author: jinxiyao
"""

def twoSum(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
            

[i,j]=twoSum([1,2,3,4],7)
print i,j