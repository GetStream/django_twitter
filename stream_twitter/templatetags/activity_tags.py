from django import template

register = template.Library()

@register.simple_tag
def render_activity(activity):
    user = activity.get(u'actor')
    user_html = '<span class="user"><a href="{link}">{user}</a></span>'\
        .format(link="/user/{0}".format(user), user=user)
    tweet_object = activity.get(u'object')

    # return a dictionary that contains parsed_text(string), hashtags(list), mentions(list)
    try:
        parsed_tweet_dict = tweet_object.parse_all()

        # return a dictionary that looks like 
        # {'hashtag0': <span>#hash</span", 'mention0': <a>@mike</a>}
        encoded = encode_tweet(parsed_tweet_dict) 

        # merge
        statement = parsed_tweet_dict.get(u'parsed_text').format(**encoded)
    except:
        statement = "Error Please investigate"
    # combine
    combined_div = '<div class="activity">{user}: \
        <span class="activity-text">{statement}</span></div>'\
        .format(user=user_html, statement=statement)
    return combined_div

def encode_tweet(parsed_tweet_dict):
    result = {}

    # adding html component to hashtags
    for index, value in enumerate(parsed_tweet_dict.get(u'hashtags')):
        result['hashtag'+str(index)] = \
            u'<span class="hashtag"><a href="{link}">{hashtag}</a></span>'\
                .format(hashtag=value, link="/hashtag/{0}"\
                    .format(value[1:]))

    # adding html component to mentions
    for index, value in enumerate(parsed_tweet_dict.get(u'mentions')):
        result['mention'+str(index)] = \
            u'<span class="mention"><a href="{link}">{mention}</a></span>'\
                .format(mention=value, link="/user/{0}"\
                    .format(value[1:]))
    return result
