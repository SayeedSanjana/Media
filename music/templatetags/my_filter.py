from django import template
register=template.Library()


def split_str(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

register.filter('split',split_str)    