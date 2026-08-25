class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <0:
            x =1/x
            n= -n

        result = 1.0
        curr_product = x

        while n > 0:
            if n % 2 == 1:
                result *= curr_product
                n = n-1
            curr_product *= curr_product
            n = n //2
        return result