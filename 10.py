#                10. Calculate Interest
amount = int(input("Please enter principal amount:"))
rate = float(input("Please Enter Rate of interest in %:"))
years = int(input("Enter number of years for investment:"))
cal = (amount*(1+rate/100)**years)
print("After",  years, "years your principal amount", amount, "over an interest rate of", rate, "% will be", cal)