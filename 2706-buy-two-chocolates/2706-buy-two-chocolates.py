class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest = float('inf')
        second_smallest = float('inf')

        for num in prices:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num

        if (smallest+second_smallest)>money:
            return money
        return (money)-(smallest+second_smallest)