from django import template

register = template.Library()

@register.simple_tag
def render_activity(activity):
    statement = "User {0} {1}: {2}".format(activity.get(u'actor'), 
        activity.get(u'verb'), activity.get(u'object').text)
    print(type(activity.get(u'actor')))
    print(type(activity.get(u'object')))
    return statement
