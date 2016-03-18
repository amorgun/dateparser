# -*- coding: utf-8 -*-
__version__ = '0.3.4'

from .date import DateDataParser
from .conf import apply_settings
from .dtime import datetime

_default_parser = DateDataParser(allow_redetect_language=True)

@apply_settings
def parse(date_string, date_formats=None, languages=None, settings=None, now=None):
    """Parse date and time from given date string.

    :param date_string:
        A string representing date and/or time in a recognizably valid format.
    :type date_string: str|unicode
    :param date_formats:
        A list of format strings using directives as given
        `here <https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>`_.
        The parser applies formats one by one, taking into account the detected languages.
    :type date_formats: list
    :param languages:
        A list of two letters language codes.e.g. ['en', 'es']. If languages are given, it will not attempt
        to detect the language.
    :type languages: list

    :param settings:
           Configure customized behavior using settings defined in :mod:`dateparser.conf.Settings`.
    :type settings: dict

    :param now:
        Current time for relative dates and filling missing values. If set to None uses current time.
    :type now: :class:`datetime <datetime.datetime>`


    :return: Returns :class:`datetime <datetime.datetime>` representing parsed date if successful, else returns None
    :rtype: :class:`datetime <datetime.datetime>`.
    :raises: ValueError - Unknown Language
    """
    parser = _default_parser

    if any([languages, not settings._default]):
        parser = DateDataParser(languages=languages, settings=settings)

    with datetime.set_now(now):
        data = parser.get_date_data(date_string, date_formats)

    if data:
        return data['date_obj']
