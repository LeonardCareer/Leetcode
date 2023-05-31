class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join([char.lower() for char in s if char.isalnum()])
        return result == result[::-1]
    
test = Solution()
input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"
input3 = " "
print(test.isPalindrome(input1))
print(test.isPalindrome(input2))
print(test.isPalindrome(input3))