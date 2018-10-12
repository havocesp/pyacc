# -*- coding: utf-8 -*-
"""
 PyACC
 - Author:      Daniel J. Umpierrez
 - Created:     12-10-2018
 - License:     UNLICENSE
"""
import time

import begin

import pyacc.utils as utils

ERROR_NULL_RESPONSE = ' - [ERROR] Null response, 5 seconds to retry ... '

MSG_RETRY_TIME = ' - Waiting to retry ... '
MSG_LAST_OUTPUT = '{:.2f} {}'

wait = time.sleep


@begin.start
@begin.convert(amount=float)
def main(from_currency, amount=1.0, to_currency=utils.Fiat.USD):
    to = str(to_currency or utils.Fiat.USD).upper()
    to = to.strip().strip('T')
    to = utils.FIAT[to] if to and to in utils.FIAT else utils.FIAT[utils.Fiat.USD]
    trade_pair = '{}/{}'.format(str(from_currency).upper(), to)

    retries = 5
    wait_secs = 5
    price = None

    try:
        while price is None and retries > 0:
            try:

                price = utils.get_price(*trade_pair.split('/'))

                if price and len(price):
                    print(MSG_LAST_OUTPUT.format(price.get(to_currency) * amount, to_currency))
                else:
                    print(ERROR_NULL_RESPONSE)

            except (ValueError, AttributeError) as err:
                print(' - [ERROR] {}.'.format(err))
                # wait_secs = 60 if 'DDoS' in str(err) else 15
                print(MSG_RETRY_TIME)
            finally:
                retries -= 1
                wait(wait_secs if price is None else 0)
                wait_secs = 5
                if price:
                    break

    except KeyboardInterrupt:
        print('Aborted')

    return 0
