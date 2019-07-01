from django import template

register = template.Library()

@register.filter
def for_subtract(value, arg):
	return range(value - arg)
@register.filter
def for_(value):
	return range(value)
@register.filter
def length(value):
	return len(value)
@register.filter
def cut(value, arg):
	return value[0:arg] + '...'
@register.filter
def get_m(value):
	return list(value.all())