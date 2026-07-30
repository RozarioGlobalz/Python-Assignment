def apply_discount(item, original_price, promo_code):

    if promo_code == "Save10":
        discount = 0.10
    elif promo_code == "HalfOFF":
        discount = 0.50
    else:
        "no_discount"

    discounted = original_price - (original_price * discount)
    return discounted

item = input("Enter item name:")

original_price = float(input("Enter the original price:"))

promo_code = input("Enter the promo code:")




print(apply_discount(item, original_price, promo_code))


#print(apply_discount("bag", 200, "Save10"))
