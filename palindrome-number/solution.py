class Solution:
    def isPalindrome(self, x: int)-> bool:
        if x < 0:
            return False
        # Else we care about if the number is palindrome
        reverse_x = self.reverse_number(x)
        if reverse_x == x:
            return True
        return False


    def reverse_number(self, x: int)-> int:
        """
        Function to reverse a number
        """
        # Thanks to Python, we dont care about overflow !!
        temp = x
        reverse_x = 0
        while temp > 0:
            rem = temp % 10
            reverse_x = reverse_x * 10 + rem
            temp = temp // 10

        return reverse_x
