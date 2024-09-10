import math
class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        rounded = math.floor((purchaseAmount + 5) / 10) * 10
        return 100 - int(rounded)