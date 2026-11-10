def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculates the discount amount based on price and discount percentage.
    Discount percentage should be between 0 and 100.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    
    discount_amount = price * (discount_percent / 100)
    return round(discount_amount, 2)


def calculate_total_with_tax(price: float, tax_rate: float = 0.05) -> float:
    """Calculates total price including tax."""
    return round(price * (1 + tax_rate), 2)
