class InsufficientBalanceError(Exception):
    pass


balance = 500
withdraw = 800

try:
    if withdraw > balance:
        raise InsufficientBalanceError(
            "Insufficient balance!"
        )

    balance -= withdraw
    print("Withdrawal successful")

except InsufficientBalanceError as e:
    print(e)