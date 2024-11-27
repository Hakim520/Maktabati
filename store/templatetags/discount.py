from django import template
from urllib.parse import urlencode, parse_qs, urlsplit, urlunsplit

register = template.Library()


@register.filter(name='discount_calculator')
def discount_calculator(price, discount):
    """Applies a discount to a price."""
    try:
        # Assuming discount is a percentage and price can be cast to float
        original_price = float(price)
        discount_percentage = float(discount)
        discounted_price = original_price * (1 - (discount_percentage / 100))
        return round(discounted_price, 2)
    except (ValueError, TypeError):
        return price  # Return the original price if there's an error