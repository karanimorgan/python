def calculate_discounted_price(price, discount=10):
    discounted = price * discount / 100
    final = price - discounted
    return final

if __name__ == "__main__":
   price = 100
   discounted_price = calculate_discounted_price(price)
print(f"The discounted price of {price} with a discount of 10% is: {discounted_price} ")