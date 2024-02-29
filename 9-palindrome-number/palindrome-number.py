class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: 
            return False
        else:
            rev = 0
            origional_num = x
            while x>0:
                rem = x%10
                rev = rev*10 + rem
                x=x//10
            return rev == origional_num

        