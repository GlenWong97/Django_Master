from django import template
import math
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

@register.filter
def sort_by(Thing, args):
	if args == 'price':
		return sorted(Thing, key=lambda t: t.price)
	elif args == '-date_posted':
		return sorted(Thing, key=lambda t: t.date_posted, reverse=True)
	elif args == '-n_subs':
		return sorted(Thing, key=lambda t: t.n_subs, reverse=True)
	elif args == '-n_rating':
		return sorted(Thing, key=lambda t: t.n_rating, reverse=True)
	else:
		return False
@register.filter
def add_(x, y):
	return x + y

@register.filter
def sigdig(value, digits = 3):
    order = int(math.floor(math.log10(math.fabs(value))))
    places = digits - order - 1
    if places > 0:
        fmtstr = "%%.%df" % (places)
    else:
        fmtstr = "%.0f"
    return fmtstr % (round(value, places))
@register.filter
def multiply_byS(value, arg):
	digits = 2
	value = float(value) * arg
	order = int(math.floor(math.log10(math.fabs(value))))
	places = digits - order - 1
	if places > 0:
		fmtstr = "%%.%df" % (places)
	else:
		fmtstr = "%.0f"
	return fmtstr % (round(value, places))
@register.filter
def strtolist(s1, separator):
	return s1.split(separator)