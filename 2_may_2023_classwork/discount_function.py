def discount(price):
    new_price = 0
    count = 0.1
    discount = price * count
    new_price = price - discount
    try:
       return f"The Discount of Price {price} is {discount} the New price is {new_price}"
    except TypeError:
        return f"Your input must be a number"


price =int(input("Enter your price: "))
print(discount(price))
