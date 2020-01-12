import socialmediafeed
import newsfeed
import json

def process_search_data(search_string: str, source='social_media'):
    # TODO: ask Rick to add parameter to adjust number of items returned by search.
    if source == 'social_media':
        search_data = process_social_media_data(search_string)
    elif source == 'news_feed':
        search_data = process_news_feed_data(search_string)
    else:
        raise NotImplementedError
    return zip(search_data['url'], search_data['text'])


def process_social_media_data(search_string):
    search_data = {'url': [], 'text': []}
    raw_data = socialmediafeed.search(search_string)
    for element in raw_data['posts']:
        for field in ('url', 'text'):
            search_data[field].append(element[field])
    return search_data


def process_news_feed_data(search_string):
    search_data = {'url': [], 'text': []}
    raw_data = json.loads(newsfeed.search(search_string))
    for element in raw_data['value']:
        search_data['url'].append(element['url'])
        search_data['text'].append(element['body'])
    return search_data


if __name__ == '__main__':
    query = 'UBC'
    sd1 = process_search_data(query, 'social_media')
    sd2 = process_search_data(query, 'news_feed')
