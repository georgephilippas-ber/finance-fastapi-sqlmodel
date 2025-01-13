from typing import Iterable

from configuration.client.eodhd import UNITED_STATES_EXCHANGE_LIST


def supported_united_states_exchange_code_list() -> Iterable[str]:
    return map(lambda exchange: exchange['Code'], UNITED_STATES_EXCHANGE_LIST)


def to_eodhd_exchange_code(exchange_code: str) -> str:
    if exchange_code in supported_united_states_exchange_code_list():
        return 'US'
    else:
        return exchange_code
