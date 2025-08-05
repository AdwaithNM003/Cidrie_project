def calculate_discount(price,percentage):
    if price<0:
        raise ValueError("Price should be positive")
    if percentage<0 or percentage>100:
        raise ValueError("Percentage is unacceptable")
    disc=(percentage*price)/100
    mrp=price-disc
    return mrp