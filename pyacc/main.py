# -*- coding: utf-8 -*-
"""PyACC

 - Author:      Daniel J. Umpierrez
 - Created:     12-10-2018
 - License:     UNLICENSE
"""
import argparse
import sys
import time

from pyacc.utils import Fiat, get_price

ERROR_NULL_RESPONSE = ' - [ERROR] Null response, 5 seconds to retry ... '
ERROR_SAME_CURRENCIES = ' - [ERROR] "From" currency ({}) and "To" currency ({}) can not be the same.'
MSG_RETRY_TIME = ' - Waiting to retry ... '



def main(args):
    assert str(args.to.upper()) != str(args.cfrom.upper()), ERROR_SAME_CURRENCIES
    to = args.to.upper().strip(' T')
    to = Fiat(to) if str(to) in Fiat.LIST else to
    retries = 5
    wait_secs = 5
    price = None

    try:
        while price is None and retries > 0:
            try:
                price = get_price(args.cfrom.upper(), to)

                if len(price or {}):
                    result = price.get(to.id) * args.amount
                    print(f'{result:.2f} {to.id}')
                else:
                    print(ERROR_NULL_RESPONSE)

            except (ValueError, AttributeError) as err:
                print(f' - [ERROR] {err}.')
            finally:
                retries -= 1
                time.sleep(wait_secs if price is None else 0)
                wait_secs = 5
                if price:
                    break
    except KeyboardInterrupt:
        print('Aborted')
    return 0


def run():
    parser = argparse.ArgumentParser(description='Fiat to cryptocurrencies converter.')
    parser.add_argument('-a', '--amount', type=float, default=1.0,
                        help='Source currency amount to be changed to (default 1.0)')
    parser.add_argument('-t', '--to', default=Fiat.USD,
                        help='Destination currency (default USD).')
    parser.add_argument('-f', '--from', dest='cfrom', default='BTC',
                        help='Source cryptocurrency (default BTC)')
    parsed_args = parser.parse_args()
    r_code = main(args=parsed_args)
    sys.exit(r_code)


if __name__ == '__main__':
    run()
