"""
Fix Bug: Corrected price calculation in trading bot

Summary:
- Fixed a bug where transaction fees were not subtracted from the user's balance.
- Added test case to verify correct behavior.

Usage:
    python "Fix Bug.py"
"""

class TradingBot:
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def buy_crypto_buggy(self, price, amount, fee_percent):
        """Old buggy method: fails to subtract fee from balance."""
        total_cost = price * amount
        fee = total_cost * fee_percent / 100
        # BUG: Fee not subtracted!
        self.balance -= total_cost
        return fee

    def buy_crypto_fixed(self, price, amount, fee_percent):
        """Fixed method: correctly subtracts fee from balance."""
        total_cost = price * amount
        fee = total_cost * fee_percent / 100
        self.balance -= (total_cost + fee)
        return fee

# Test case
if __name__ == "__main__":
    bot = TradingBot(1000)
    print("Initial balance: $", bot.balance)
    fee = bot.buy_crypto_buggy(price=100, amount=5, fee_percent=1)
    print("After buggy buy: $", bot.balance, "| Fee charged:", fee)

    # Reset
    bot = TradingBot(1000)
    fee = bot.buy_crypto_fixed(price=100, amount=5, fee_percent=1)
    print("After fixed buy: $", bot.balance, "| Fee charged:", fee)