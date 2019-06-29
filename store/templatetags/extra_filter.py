from django import template

register = template.Library()

@register.filter
def for_subtract(value, arg):
	return range(value - arg)
@register.filter
def for_(value):
	return range(value)