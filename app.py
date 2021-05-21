def dividend_value(shares, dividend):
    value = shares * dividend
    return value

shares = int(input("Provide number of Tyson food shares:\n"))
dividend = 0.445
value = dividend_value(shares,  dividend)
print(f"The value of dividend is: {value} usd")