def maxProfit(self, prices: List[int]) -> int:
        buy_ptr = 0
        sell_ptr = buy_ptr+1
        max_prof = 0
        while (sell_ptr<len(prices)):
            prof = prices[sell_ptr] - prices[buy_ptr]
            # print('buy_ptr => ',buy_ptr)
            # print('sell_ptr => ',sell_ptr)
            if(prof >max_prof):
                max_prof = prof

            if(prices[buy_ptr] > prices[sell_ptr]):
                buy_ptr = sell_ptr
                sell_ptr +=1
            else:
                sell_ptr +=1
        return max_prof