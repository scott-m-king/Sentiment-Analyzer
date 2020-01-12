import socialmediafeed
import newsfeed
import nlp
import json
import matplotlib.pyplot as plt
import mpld3
import os
import time


def process_search_data(search_string: str, source='social_media'):
    """

    :param search_string:
    :param source:
    :return:
    """
    # TODO: ask Rick to add parameter to adjust number of items returned by search.
    if source == 'social_media':
        search_data = process_social_media_data(search_string)
    elif source == 'news_feed':
        search_data = process_news_feed_data(search_string)
    else:
        raise NotImplementedError
    sentiments = (nlp.analyze_sentiment(text) for text in search_data['text'])
    return search_data['url'], list(sentiment.document_sentiment.score for sentiment in sentiments)


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


def bar_plot_scores(scores):
    y = scores
    x = list(range(len(y)))
    z = sum(y)/len(y)
    fig = plt.figure()
    ax = fig.gca()
    ax.bar(x, y)
    ax.plot(x, [z for _ in x], 'k--')
    filename = 'static/bar_{:d}.png'.format(int(time.time()))
    plt.savefig(filename)
    return z


def bar_plot_most_recent_filename():
    files = filter(lambda file: 'bar' in file and len(file) == 18, os.listdir('static/'))
    file = max(files, key=lambda s: s[4:-4])
    return 'static/' + file


def pie_plot_scores(scores, threshold=(-0.4, 0.4)):
    values = [0, 0, 0]
    for score in scores:
        if score < threshold[0]:
            values[0] += 1
        elif score < threshold[1]:
            values[1] += 1
        else:
            values[2] += 1
    fig = plt.figure()
    ax = fig.gca()
    plt.pie(values,
            labels=['negative', 'neutral', 'positive'],
            colors=['red', 'yellow', 'green'])
    filename = 'static/pie_{:d}.png'.format(int(time.time()))
    plt.savefig(filename)
    return 0


def pie_plot_most_recent_filename():
    files = filter(lambda file: 'pie' in file and len(file) == 18, os.listdir('static/'))
    file = max(files, key=lambda s: s[4:-4])
    return 'static/' + file



if __name__ == '__main__':
    pass
    # query = 'UBC'
    # url1, scores1 = process_search_data(query, 'social_media')
    # url2, scores2 = process_search_data(query, 'news_feed')
    # fig = bar_plot_scores(scores1 + scores2)
    # mpld3.show(fig)

