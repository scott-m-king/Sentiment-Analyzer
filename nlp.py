# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

if __name__ == '__main__':

    # Instantiates a client
    client = language.LanguageServiceClient.from_service_account_json('key.json')

    # The text to analyze
    text = 'Terrible work!'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment


    from google.cloud import language_v1
    from google.cloud.language_v1 import enums


    def sample_analyze_syntax(text_content):
        """
        Analyzing Syntax in a String

        Args:
          text_content The text content to analyze
        """

        client = language_v1.LanguageServiceClient.from_service_account_json('key.json')

        # text_content = 'This is a short sentence.'

        # Available types: PLAIN_TEXT, HTML
        type_ = enums.Document.Type.PLAIN_TEXT

        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": text_content, "type": type_, "language": language}

        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = enums.EncodingType.UTF8

        response = client.analyze_syntax(document, encoding_type=encoding_type)
        # Loop through tokens returned from the API
        for token in response.tokens:
            # Get the text content of this token. Usually a word or punctuation.
            text = token.text
            print(u"Token text: {}".format(text.content))
            print(
                u"Location of this token in overall document: {}".format(text.begin_offset)
            )
            # Get the part of speech information for this token.
            # Parts of spech are as defined in:
            # http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf
            part_of_speech = token.part_of_speech
            # Get the tag, e.g. NOUN, ADJ for Adjective, et al.
            print(
                u"Part of Speech tag: {}".format(
                    enums.PartOfSpeech.Tag(part_of_speech.tag).name
                )
            )
            # Get the voice, e.g. ACTIVE or PASSIVE
            print(u"Voice: {}".format(enums.PartOfSpeech.Voice(part_of_speech.voice).name))
            # Get the tense, e.g. PAST, FUTURE, PRESENT, et al.
            print(u"Tense: {}".format(enums.PartOfSpeech.Tense(part_of_speech.tense).name))
            # See API reference for additional Part of Speech information available
            # Get the lemma of the token. Wikipedia lemma description
            # https://en.wikipedia.org/wiki/Lemma_(morphology)
            print(u"Lemma: {}".format(token.lemma))
            # Get the dependency tree parse information for this token.
            # For more information on dependency labels:
            # http://www.aclweb.org/anthology/P13-2017
            dependency_edge = token.dependency_edge
            print(u"Head token index: {}".format(dependency_edge.head_token_index))
            print(
                u"Label: {}".format(enums.DependencyEdge.Label(dependency_edge.label).name)
            )

        # Get the language of the text, which will be the same as
        # the language specified in the request or, if not specified,
        # the automatically-detected language.
        print(u"Language of the text: {}".format(response.language))

    sample_analyze_syntax("Great job, everyone!")
