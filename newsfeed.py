import requests
import json


def search(query):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"
    querystring = {"autoCorrect": "false", "pageNumber": "1", "pageSize": "50", "q": query, "safeSearch": "false"}
    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "f3512dba28msha0bfafff623f90fp18ccabjsn78a20a660e54"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


if __name__ == '__main__':
    data = json.loads(search('UBC'))

    for i in data['value']:
        print(i['title'])
        # print(i['description'])
        # print(i['url'])
