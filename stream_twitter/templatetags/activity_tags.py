from django import template

register = template.Library()

@register.simple_tag
def render_activity(activity):
    user = '<span class="user">{0}</span>'.format(activity.get(u'actor'))
    verb = '<span class="verb">{0}</span>'.format(activity.get(u'verb'))
    statement = '<div class="activity">{0} {1}: \
        <span class="activity-text">{2}</span></div>'\
        .format(user, verb, activity.get(u'object').text)
    return statement