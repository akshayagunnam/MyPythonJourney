"""Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

"""
class Solution:
    def isPalindrome(self, head):
        lis=[]
        while head!=None:
            lis.append(head.val)
            head=head.next
        length=len(lis)
        i=0
        j=length-1
        while i<=j:
            if lis[i]==lis[j]:
                i+=1
                j-=1
                continue
            else:
                return False
        return True
