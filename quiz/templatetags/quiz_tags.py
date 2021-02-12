from django import template

register = template.Library()


@register.filter(name="cssadd")
def cssadd(field, css):
    return field.as_widget(attrs={"class":css})
