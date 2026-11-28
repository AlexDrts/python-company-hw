from django import template

register = template.Library()


@register.filter
def initials(value):
    return ''.join(part[0] for part in str(value).split()).upper()


@register.filter
def phone(value):
    digits = ''.join(ch for ch in str(value) if ch.isdigit())
    if len(digits) != 11:
        return value
    return f'+{digits[0]} {digits[1:4]} {digits[4:7]} {digits[7:]}'
