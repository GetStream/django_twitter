from django import template

register = template.Library()

@register.simple_tag
def render_activity(activity):
    statement = "User {0} {1}: {2}".format(activity.get(u'actor'), 
        activity.get(u'verb'), activity.get(u'object').text)
    return statement
