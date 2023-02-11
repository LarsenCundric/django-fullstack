from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values from "arg" from the string
    """

    return value.replace(arg, '')

# Can also do this: (not common)
# register.filter('cut', cut)