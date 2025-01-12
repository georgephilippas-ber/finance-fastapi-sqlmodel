from typing import Iterable, List

UNITED_STATES_EXCHANGE_LIST = [
    {
        "Name": "New York Stock Exchange",
        "Code": "NYSE",
        "OperatingMIC": "XNYS",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    },
    {
        "Name": "NASDAQ Stock Exchange",
        "Code": "NASDAQ",
        "OperatingMIC": "XNAS",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    },
    {
        "Name": "Chicago Board Options Exchange",
        "Code": "CBOE",
        "OperatingMIC": "XCBO",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    },
    {
        "Name": "Chicago Stock Exchange",
        "Code": "CHX",
        "OperatingMIC": "XCHI",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    },
    {
        "Name": "Investors Exchange",
        "Code": "IEX",
        "OperatingMIC": "IEXG",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    }
]


def supported_united_states_exchange_code_list() -> Iterable[str]:
    return map(lambda exchange: exchange['Code'], UNITED_STATES_EXCHANGE_LIST)


def to_eodhd_exchange_code(exchange_code: str) -> str:
    if exchange_code in supported_united_states_exchange_code_list():
        return 'US'
    else:
        return exchange_code


EODHD_DEMO: bool = False
EODHD_EXCHANGES: List[str] = ["XETRA", "F"]
EODHD_OVERRIDE_TICKERS = [("AAPL", "NASDAQ"), ("AMZN", "NASDAQ"), ("MSFT", "NASDAQ"), ("TSLA", "NASDAQ")]
