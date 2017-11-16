import six
import json
import urllib2

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from bs4 import BeautifulSoup


# <export GOOGLE_APPLICATION_CREDENTIALS=<path-to-credentials.json>

def entities_text(text):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    important_words = []
    for entity in entities:
        important_words.append(
            (entity.name, entity_type[entity.type], entity.salience))

    return important_words


def sentiment_text(text):
    """Detects sentiment in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    sentiment = client.analyze_sentiment(document).document_sentiment

    return sentiment.score, sentiment.magnitude


resp = urllib2.urlopen('http://96.242.223.244/news_aggregator/display.php')
soup = BeautifulSoup(resp, "html.parser",
                     from_encoding=resp.info().getparam('charset'))

article_titles_list = []
for link in soup.find_all('a', href=True):
    article_titles_list.append(link.string)


for text in article_titles_list:
    print entities_text(text), sentiment_text(text)







