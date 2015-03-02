from django import template

register = template.Library()

@register.simple_tag
def render_user(user):
    print("\n####{0}####\n".format(user.username))
    picture = '<div class="user-picture"><a href="{link}"><img src="{picture}"></a></div>'\
        .format(picture=user.userprofile.picture.url, link="/user/{0}".\
            format(user.username))
    text = '<div class="hashtag"><a href="{link}">{user}</a></div>'\
        .format(user=user.username, link="/user/{0}"\
            .format(user.username))
    html = "{0}{1}".format(picture, text)
    return html