from django import template

register = template.Library()

@register.filter
def for_subtract(value, arg):
	x = int(arg)
	return range(value - x)
@register.filter
def for_(value):
	value = abs(int(value))
	return range(value)
@register.filter
def length(value):
	return len(value)
@register.filter
def cut(value, arg):
	if arg >= len(value):
		return value
	return value[0:arg] + '...'
@register.filter
def cutb(value, arg):
	x = len(value) - 1
	return value[arg:x]
@register.filter
def get_m(value):
	return list(value.all())
@register.filter
def calc_rating(feedback):
	feedback = list(feedback.all())
	total_rating = 0
	number_of_rating = 0
	for i in feedback:
		if i.rating >= 0 and i.rating <= 5:
			total_rating += i.rating
			number_of_rating += 1
	if number_of_rating == 0:
		return 0
	return (float(total_rating) /number_of_rating)* 20
@register.filter
def multiply_by(value, arg):
	return round(value * arg, 2)
@register.filter
def legit_count(value):
	n = 0
	for i in value:
		if i.rating >= 0:
			n += 1
	return n
@register.filter
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)

@register.filter
def split_this(value):
	return value.split()