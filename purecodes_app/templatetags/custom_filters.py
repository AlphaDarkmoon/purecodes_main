from django import template

register = template.Library()

@register.filter
def slice_list(lst, start):
    return lst[start:]
