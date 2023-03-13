print("Enter revenue:")
revenue = int(input())

print("Enter cost:")
costs = int(input())

financial_result = revenue - costs

if financial_result > 0:
    print(f"Financial result is profit. Its value is {financial_result}")
    profitability = financial_result / revenue
    print(f"The profitability of revenue is {profitability}")

    print("Enter count of employees:")
    employees = int(input())
    profit_per_employee = financial_result / employees
    print(f"Company profit per employee is {profit_per_employee}")
elif financial_result == 0:
    print(f"Financial result is without profit and loss.")
else:
    print(f"Financial result is loss.")
