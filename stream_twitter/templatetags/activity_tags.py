from django import template

register = template.Library()

@register.simple_tag
def render_activity(activity):
    user = '<span class="user">{0}</span>'.format(activity.get(u'actor'))
    verb = '<span class="verb">{0}</span>'.format(activity.get(u'verb'))
    tweet_object = activity.get(u'object')

    # return a dictionary that contains parsed_text(string), hashtags(list), mentions(list)
    parsed_tweet_dict = tweet_object.parse_all()

    # return a dictionary that looks like 
    # {'hashtag0': <span>#hash</span", 'mention0': <a>@mike</a>}
    encoded = encode_tweet(parsed_tweet_dict) 

    # merge
    statement = parsed_tweet_dict.get(u'parsed_text').format(**encoded)

    # combine
    combined_div = '<div class="activity">{0} {1}: \
        <span class="activity-text">{2}</span></div>'\
        .format(user, verb, statement)
    return combined_div

def encode_tweet(parsed_tweet_dict):
    result = {}

    for index, value in enumerate(parsed_tweet_dict.get(u'hashtags')):
        result['hashtag'+str(index)] = \
            u'<span class="hashtag"><a href={link}>{hashtag}</a></span>'\
                .format(hashtag=value, link="") #TBI link address

    for index, value in enumerate(parsed_tweet_dict.get(u'mentions')):
        result['mention'+str(index)] = \
            u'<span class="mention"><a href={link}>{mention}</a></span>'\
                .format(mention=value, link="") #TBI link address
    return result
