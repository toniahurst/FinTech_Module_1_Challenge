# coding: utf-8
import csv
from pathlib import Path

# Part 1: Automate the Calculations.

loan_costs = [500, 600, 200, 1000, 450]

"""How many loans are in the list?
Use the `len` function to calculate the total number of loans in the list.
Print the number of loans from the list
"""
number_of_loans = len(loan_costs)
print("")
print("* * * * * * * * * * * * * * * * * * * PART 1 * * * * * * * * * * * * * * * * * * * *\n")
print(f"The number of loans on the list is: {number_of_loans}\n")

# Use the `sum` function to calculate the total of all loans in the list.
# Print the total $# value of the loans
total_of_all_loans = sum(loan_costs)
print(f"The total value of all loans is: ${total_of_all_loans:0.2f}\n")

# Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
average_loan_amount = total_of_all_loans / number_of_loans
print(f"The average loan amount is: ${average_loan_amount:.02f}\n")
print("")
print("* * * * * * * * * * * * * * * * * * * PART 2 * * * * * * * * * * * * * * * * * * * *\n")

# Part 2: Analyze Loan Data.
# Use get to extract values, saves these values to variables, and print each variable

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The fuuture value  of the loan is: ${future_value}\n")
print(f"The number of months remaining in the loan is: {remaining_months}\n")


# Use the formula for Present Value to calculate a "fair value" of the loan using a
# minimum required return of 20% as the discount rate.
# Use the **monthly** version of the present value formula 
# (Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months)
annual_discount_rate = 0.20
fair_value = future_value / (1 + annual_discount_rate/12) ** remaining_months

# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price")
if fair_value >= loan_price:
    print(f"Buy this loan! It costs ${loan_price:0.2f} and is worth ${fair_value:0.2f}.")
else:
    print(f"Don't buy this loan! It costs ${loan_price:0.2f} and is worth ${fair_value:0.2f}.")


# Part 3: Perform Financial Calculations.
# Define a new function that will be used to calculate present value.
# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
print("")
print("* * * * * * * * * * * * * * * * * * * PART 3 * * * * * * * * * * * * * * * * * * * *\n")
future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")
annual_discount_rate = 0.2


# Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / ((1 + annual_discount_rate/12)**remaining_months)
    return present_value

# Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
npv = calculate_present_value(future_value, remaining_months, annual_discount_rate)

print(f"The present value of the loan is: ${npv:0.2f}")

# Part 4: Conditionally filter lists of loans.
# Use a loop to iterate through a series of loans and select only the inexpensive loans.
# Create a new, empty list called `inexpensive_loans`.
# Use a for loop to select each loan from a list of loans.
# a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
# b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
# Print the list of inexpensive_loans.

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

print("")
print("* * * * * * * * * * * * * * * * * * * PART 4 * * * * * * * * * * * * * * * * * * * *\n")

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    
    temp = loan["loan_price"]
    if temp <= 500:
        inexpensive_loans.append(loan)
    else:
        ("")

# @TODO: Print the `inexpensive_loans` list
number_of_loans = len(inexpensive_loans)
print(f"There are {number_of_loans} loans <= $500\n")

count = 0
for loan in inexpensive_loans:
    print(f"Inexpensive loan number {count + 1} is: {inexpensive_loans[count]}\n")
    count = count + 1 
     

"""Part 5: Save the results

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects
"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
csvpath = Path("inexpensive_loans.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # write the header rows
    csvwriter.writerow(header)

    # write the data rows
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())

print("")
print("* * * * * * * * * * * * * * * * * * * PART 5 * * * * * * * * * * * * * * * * * * * *\n")
print(f"Writing inexpensive loans to file...\n")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")