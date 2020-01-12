# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums


def analyze_sentiment(text: str):
    """
    Performs a sentiment analysis on the input string.

    Returns magnitude and score of sentiment.

    :param text:
    Input string.

    :return:
    sentiment (type google.cloud.languave_v1.types.AnalyzeSentimentResponse).

    sentiment.document_sentiment
        - measure of sentiment of whole document
        - fields:
            magnitude
            score

    sentiment.sentences
        - list of sentences in the document, each of which has magnitude and score fields
    """
    return __analyze(text, 'sentiment')


def analyze_entities(text: str):
    """
    Performs an entity analysis on the input string.

    Returns all the entities referred to in the string.

    :param text:
    Input string.

    :return:
    Entities (type google.cloud.language_v1.types.AnalyzeEntitiesResponse).

    entities.entities
        - list of entities with fields:
            - name
            - type
            - salience
            - mentions
    """
    return __analyze(text, 'entities')


def analyze_entity_sentiment(text: str):
    """
    Performs a combination entity/sentiment analysis on the input text.

    Returns all entity/sentiments referred to in the string.

    :param text:
    Input string.

    :return:
    entity_sentiment (type google.cloud.language_v1.types.AnalyzeEntitySentimentResponse).

    entity_sentiment.entities
        - list of entities with fields:
            - name
            - type
            - salience
            - mentions
            - sentiment
                - magnitude
                - score
    """
    return __analyze(text, 'entity-sentiment')


def analyze_syntax(text: str):
    """
    Performs syntax analysis on the input string.

    Returns syntax for each token in the sentence.

    :param text:
    Input string.

    :return:
    entity_sentiment (type google.cloud.language_v1.types.AnalyzeSyntaxResponse).
    """
    return __analyze(text, 'syntax')


def classify_text(text: str):
    """
    Performs a classification of the input string.

    :param text:
    Input string.

    :return:
    classification (type google.cloud.language_v1.types.ClassifyTextResponse).

    classification.categories
        - list of categories with fields
            - name
            - confidence

    """
    return __analyze(text, 'classification')


def __analyze(text: str, analysis_level: str):
    client = language.LanguageServiceClient.from_service_account_json('key.json')
    document = {"content": text, "type": enums.Document.Type.PLAIN_TEXT, "language": 'en'}
    analyses = {'sentiment': client.analyze_sentiment,
                'entities': client.analyze_entities,
                'entity-sentiment': client.analyze_entity_sentiment,
                'syntax': client.analyze_syntax,
                'classification': client.classify_text}
    try:
        result = analyses[analysis_level.lower()](document)
        return result
    except KeyError:
        raise NotImplementedError


if __name__ == '__main__':
    test_text = 'I’m a high school student in Nanaimo currently choosing between UBC and VIU. ' \
                'My parents are putting aside 20k for me. ' \
                'If I go to VIU, I will live with my parents and I won’t have to work or pay for food. ' \
                'I’ll graduate with no debt. ' \
                'If I go to UBC, I’ll be over 100k in debt at graduation. ' \
                'I’m sick of Nanaimo and love the city. ' \
                'I’m also pretty diligent when it comes to academic success, and love competition. ' \
                'What seems like the better school in my circumstance?'

    sentiment = analyze_sentiment(test_text)
    entities = analyze_entities(test_text)
    entity_sentiment = analyze_entity_sentiment(test_text)
    syntax = __analyze(test_text, 'syntax')
    classification = __analyze(test_text, 'classification')
