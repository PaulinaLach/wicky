from django import template

register = template.Library()

@register.filter(name='name')
def name(first_name, last_name):
    return first_name + " " + last_name