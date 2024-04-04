# Practice in Class 1: Purchase Receipt
# 1: get input
name = str(input("Enter name:"))
purchase = float(input("Enter purchase price:"))
# 2: calculate amounts
tax_rate = 0.1
tax = purchase * tax_rate
total = purchase + tax
# 3: format amounts
p = format(purchase, ',.2f')
t = format(tax, ',.2f')
tot = format(total, ',.2f')
# 4: print out amounts
print("Hello {}, here is your sales receipt:".format(name))
print("Subtotal = $ ", p.rjust(7, ' '))
print("     Tax = $ ", t.rjust(7, ' '))
print("             --------")
print("   Total = $ ", tot.rjust(7, ' '))
