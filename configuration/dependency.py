from enum import Enum
from typing import Dict, Tuple, List


class ModelSliceEnum(str, Enum):
    COUNTRY_CURRENCY = "country_currency"
    GICS = "gics"
    EXCHANGE = "exchange"
    TICKER = "ticker"
    COMPANY = "company"


SEED_ENTITIES: Dict[ModelSliceEnum, Tuple[bool, List[ModelSliceEnum]]] = {
    ModelSliceEnum.COUNTRY_CURRENCY: (True, []),
    ModelSliceEnum.GICS: (True, []),
    ModelSliceEnum.EXCHANGE: (True, [ModelSliceEnum.COUNTRY_CURRENCY]),
    ModelSliceEnum.TICKER: (False, [ModelSliceEnum.EXCHANGE]),
    ModelSliceEnum.COMPANY: (
        True, [ModelSliceEnum.TICKER, ModelSliceEnum.COUNTRY_CURRENCY, ModelSliceEnum.GICS, ModelSliceEnum.EXCHANGE])
}
