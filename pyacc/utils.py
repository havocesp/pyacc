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
        resp = req.get(url, params=params or dict(), timeout=60)
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


def get_price(fsym, tsym):
    fsym = fsym.id if isinstance(fsym, Fiat) else fsym
    tsym = tsym.id if isinstance(tsym, Fiat) else tsym
    return _query(_PRICE_URL, {'fsym': fsym, 'tsyms': [tsym]})


class Meta(ABCMeta):

    def __getitem__(cls, item):
        return getattr(cls, item)


class Fiat:
    """Fiat currency class model."""
    __metaclass__ = Meta

    LIST = ['EUR', 'USD', 'GBP']
    EUR, USD, GBP = LIST

    def __init__(self, id_3=None, name=None, symbol=None):
        """Class constructor.

        :param str id_3: currency three chars identifier ("EUR", "USD", "GBP", ...)
        :param str name: english language name ("Euro", "Dollar", "Pound", ...)
        :param str symbol: currency official char symbol ("€", "$", "£", ...)
        """
        self.id = str(id_3 or '').strip().upper()
        assert self.id in self.LIST
        self.name = str(name or '')
        self.symbol = str(symbol or '')

    def __str__(self):
        return self.id or str()

    def __repr__(self):
        return str(self.id)

    def get(self, item):
        id_3 = str(item or '').strip().upper()
        return vars(self).get(id_3)

# FIAT = {
#     Fiat.EUR: Fiat(name='Euro', symbol='€'),
#     Fiat.USD: Fiat(name='Dollar', symbol='$'),
#     Fiat.GBP: Fiat(name='Pound', symbol='£')
# }
