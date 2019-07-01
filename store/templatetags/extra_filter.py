from django import template

register = template.Library()

@register.filter
def for_subtract(value, arg):
	x = int(arg)
	return range(value - x)
@register.filter
def for_(value):
	value = int(value)
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
@register.filter
def calc_rating(feedback):
	if len(feedback.all()) == 0:
		return 0
	feedback = list(feedback.all())
	total_rating = 0
	number_of_rating = 0
	for i in feedback:
		number_of_rating += 1
		total_rating += i.rating
	return (float(total_rating) /number_of_rating)* 20
@register.filter
def multiply_by(value, arg):
	return round(value * arg, 2)