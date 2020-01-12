import urllib.request as request
import json


def search(q):
    with request.urlopen('http://api.social-searcher.com/v2/search?q=' + q + '&network=web&key'
                         '=d71117332fbabd9bdfcac0737e08d1ee') as response:
        source = response.read()
        data = json.loads(source)
        return data


if __name__ == '__main__':
    data = search('nwHacks')

    for i in data['posts']:

        print(i['postid'] + "   " + i['text'])
