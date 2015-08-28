# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def text_transform_vocabulary(context):
    """Vocabulary with all available portal_transform transformations.
    """
    terms = []
    terms.append(
        SimpleTerm(
            value='text/plain',
            token='text/plain',
            title='Plain text'))
    terms.append(
        SimpleTerm(
            value='text/html',
            token='text/html',
            title='HTML'))
    terms.append(
        SimpleTerm(
            value='text/x-web-markdown',
            token='text/x-web-markdown',
            title='Markdown'))
    terms.append(
        SimpleTerm(
            value='text/x-web-intelligent',
            token='text/x-web-intelligent',
            title='Intelligent text'))
    return SimpleVocabulary(terms)
