from django import template

register = template.Library()


@register.simple_tag
def render_hashtag(hashtag):
    html = '<div class="hashtag"><a href="{link}">{hashtag}</a></div>'\
        .format(hashtag=hashtag.name, link="/hashtag/{0}"
                .format(hashtag.name))
    return html
