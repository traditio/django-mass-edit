from django import template

register = template.Library()

@register.filter
def is_readonly(field):
    return getattr(field, 'is_readonly', False)
