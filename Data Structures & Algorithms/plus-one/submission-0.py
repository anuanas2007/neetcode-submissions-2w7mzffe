class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        carry = 1

        for i in range(len(digits)):
            if digits[i] + carry < 10:
                digits[i] += carry
                digits.reverse()
                return digits
            else:
                digits[i] = 0
        
        digits.append(1)
        digits.reverse()
        return digits
            
