from typing import List

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

EODHD_DEMO: bool = False
EODHD_EXCHANGES: List[str] = ["US", ]
EODHD_OVERRIDE_TICKERS = [("AAPL", "NASDAQ"), ("AMZN", "NASDAQ"), ("MSFT", "NASDAQ"), ("TSLA", "NASDAQ")]

EODHD_BASE_URL = "https://eodhd.com"
