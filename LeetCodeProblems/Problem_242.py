"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = [*s]
        list2 = [*t]
        if len(list1) != len(list2):
            return False  
        if list1.count(list1[0]) != list2.count(list1[0]):
            return False
        check =  all(item in list1 for item in list2)
        if check is True:
            return True
        else: 
            return False 
