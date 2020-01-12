# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

if __name__ == '__main__':
    print('test cloud')

    # Instantiates a client
    client = language.LanguageServiceClient.from_service_account_json('key.json')

    # The text to analyze
    text = u'Terrible work!'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

