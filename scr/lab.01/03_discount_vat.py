# Чек: скидка и НДС
price = float(input("price: "))
discount = float(input("discount: "))
vat = float(input("vat: "))
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽\nНДС:               {vat_amount:.2f} ₽\nИтого к оплате:    {total:.2f} ₽")
