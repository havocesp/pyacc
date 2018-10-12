# -*- coding: utf-8 -*-
"""
 PyACC
 - Author:      Daniel J. Umpierrez
 - Created:     12-10-2018
 - License:     UNLICENSE
"""
from abc import ABCMeta

import requests as req

_PRICE_URL = 'https://min-api.cryptocompare.com/data/price'
_PRICE_MULTI_URL = 'https://min-api.cryptocompare.com/data/pricemulti'


def _query(url, params=None):
    result = None
    try:
        resp = req.get(url, params=params or dict())
        if resp and resp.ok:
            result = resp.json()
        elif resp:
            resp.raise_for_status()
        else:
            return None
    except req.exceptions.RequestException as err:
        print(' - ', type(err), ': ', str(err))
        result = None
    return result


def get_price(fsyms, tsyms):
    if isinstance(fsyms, str):
        fsyms = [fsyms]
    if isinstance(tsyms, str):
        tsyms = [tsyms]

    if len(fsyms) == 1 and len(tsyms) >= 1:
        fsym = str(fsyms[0])
        del fsyms
        return _query(_PRICE_URL, locals())
    elif len(fsyms) > 1 and len(tsyms) >= 1:
        return _query(_PRICE_MULTI_URL, locals())


class Meta(ABCMeta):

    def __getitem__(cls, item):
        return getattr(cls, item)


class Fiat:
    """
    Fiat currency class model.
    """
    __metaclass__ = Meta

    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'

    LIST = [EUR, USD, GBP]

    def __init__(self, id_3=None, name=None, symbol=None):
        """
        Class constructor.

        :param str id_3: currency three chars identifier ("EUR", "USD", "GBP", ...)
        :param str name: english language name ("Euro", "Dollar", "Pound", ...)
        :param str symbol: currency official char symbol ("€", "$", "£", ...)
        """
        id_3 = str(id_3 or '').strip().upper()
        assert id_3 in self.LIST
        self.id = str(id_3 or '').strip().upper()
        self.name = str(name or '')
        self.symbol = str(symbol or '')

    def __str__(self):
        return self.id or str()

    def __repr__(self):
        return str(self)

    def get(self, item):
        id_3 = str(item or '').strip().upper()
        return vars(self).get(id_3)


FIAT = {
    Fiat.EUR: Fiat(Fiat.EUR, name='Euro', symbol='€'),
    Fiat.USD: Fiat(Fiat.USD, name='Dollar', symbol='$'),
    Fiat.GBP: Fiat(Fiat.GBP, name='Pound', symbol='£')
}
