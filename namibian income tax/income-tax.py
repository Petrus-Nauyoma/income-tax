# Namibian Income Tax Brackets 2021/22
# Reference https://www.pwc.com/na/en/assets/pdf/namibia-tax-reference-and-rate-card-2021.pdf
income = float(input("Enter your annual income here: "))

if income<50000:
    print("Your income is not taxable.")

elif income>=50000 and income<100000:
    taxable = 0.18 * (income - 50000)
    print("Your income falls in the 500 001 - 100 000 tax bracket")
    print(taxable)

elif income>=100000 and income<300000:
    taxable = 9000 + 0.25*(income - 100000)
    print("Your income falls in the 100 001 - 300 000 tax bracket")
    print(taxable)

elif income>=300000 and income<500000:
    taxable = 59000 + 0.28*(income - 300000)
    print("Your income falls in the 300 001 - 500 000 tax bracket")
    print(taxable)

elif income>=500000 and income<800000:
    taxable = 115000 + 0.3*(income - 500000)
    print("Your income falls in the 500 001 - 800 000 tax bracket")
    print(taxable)

elif income>=800000 and income<1500000:
    taxable = 205000 + 0.32*(income - 800000)
    print("Your income falls in the 800 001 - 1 500 000 tax bracket")
    print(taxable)

elif income>=1500000:
    taxable = 429000 + 0.37*(income - 1500000)
    print("Your income falls above the 1 500 000 tax bracket")
    print(taxable)

else:
    print("You have entered an incorrect income amount")