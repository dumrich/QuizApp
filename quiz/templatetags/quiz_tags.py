from django import template

register = template.Library()


@register.filter(name="cssadd")
def cssadd(field, css):
    return field.as_widget(attrs={"class":css})


@register.filter(name="get_item")
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name="turn_zip")
def turn_zip(dictionary):
    return zip(dictionary.keys(), dictionary.values())