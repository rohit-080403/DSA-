class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        even_slots = (n+1) // 2
        odd_slots = n //2

        total_even_slots = pow(5 , even_slots , MOD)
        total_odd_slots = pow(4 , odd_slots , MOD)

        return (total_even_slots * total_odd_slots) % MOD