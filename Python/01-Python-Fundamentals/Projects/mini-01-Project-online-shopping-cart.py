name       = input("Enter Customer Name:")
age        = int(input("Enter Your Age:"))
prd_name1  = input("Enter Product Name 1")
prd_name2  = input("Enter Product Name 2")
prd_price1 = float(input(f"Enter price of {prd_name1}: ₹ "))
prd_price2 = float(input(f"Enter price of {prd_name2}: ₹"))
disc_percentage = float(input("Enter discount percetnage:"))

total_bill = prd_price1 + prd_price2
discount_amount = total_bill*disc_percentage/100
final_amount = total_bill - discount_amount
avg_price = total_bill/2
tax = final_amount*18//100
gst = final_amount % 10

is_adult = age >= 18
is_total = total_bill >= 1000
is_same_price = prd_price1 == prd_price2
is_cheap = prd_price1 < 500
free_delievery = is_adult and is_total
special_coupon = total_bill > 5000 or age >=60
is_not_minor = not(age < 18)

print("\n" + "="*40)
print("    🧾 SHOPPING BILL")
print("="* 40)

print("Customer:" + name)
print("Age:"+ str(age))
print("-"*40)
print(f"{prd_name1}: ₹{prd_price1} ")
print(f"{prd_name2}: ₹{prd_price2} ")
print("-"*40)
print(f"Total Bill:   ₹{total_bill} ")
print(f"Discount ({disc_percentage}%):  ₹{discount_amount}")
print(f"Final Amount:     ₹{final_amount}")
print(f"Average Price:    ₹{avg_price}")
print(f"Tax (18% floor):  ₹{tax}")
print(f"Remainder (%10):  ₹{gst}")
print("-" * 40)

# Boolean output (True/False)
print(f"Adult (18+)?        → {is_adult}")
print(f"Big Order (>₹1000)? → {is_total}")
print(f"Same Price?         → {is_same_price}")
print(f"Free Delivery?      → {free_delievery}")
print(f"Special Coupon?     → {special_coupon}")
print(f"Not a Minor?        → {is_not_minor}")
print("=" * 40)


