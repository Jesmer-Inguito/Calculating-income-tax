# pseudocode

# Create a function to calculate tax
def income_tax(income):
    # If income <= 10,000
    if income <= 10000:
        payable_tax = 0
    # If income <= 20,000
    elif income <= 20000:
        payable_tax = (income - 10000) * 0.10
    # else
    else:
        payable_tax = 10000 * 0.10 + (income - 20000) * 0.20
   
    return payable_tax

# Ask for income

# Create variable to call the function

# Print Income and Tax