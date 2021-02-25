# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

print("Month  Total Paid   Principal")

while principal > 0:

    month += 1

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

    if principal <= 0:
        principal = 0

    print(f"{month}       {total_paid:>0.2f}     {principal:<0.2f}")


print("Total paid", round(total_paid, 2))
print("Total months taken to pay:", month)
