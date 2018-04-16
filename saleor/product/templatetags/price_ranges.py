from django import template

register = template.Library()


@register.inclusion_tag('product/_price_range.html', takes_context=True)
def price_range(context, price_range):
    display_gross = context['site'].settings.display_gross_prices
    return {'price_range': price_range, 'display_gross': display_gross}


@register.simple_tag(takes_context=True)
def price_to_display(context, price):
    """Return price to display (gross or net) depending on settings."""
    display_gross = context['site'].settings.display_gross_prices
    return price.gross if display_gross else price.net
