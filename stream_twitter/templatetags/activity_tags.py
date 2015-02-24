from django import template

register = template.Library()

@register.simple_tag
def render_activity(activity):
    user = '<span class="user">{0}</span>'.format(activity.get(u'actor')
    verb = '<span class="verb">{0}</span>'.format(activity.get(u'verb'))
    statement = '{0} {1}: {2}'.format(user, verb, activity.get(u'object').text)
    return statement
