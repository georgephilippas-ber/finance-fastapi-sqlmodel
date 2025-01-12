from enum import Enum
from typing import Dict, Tuple, List


class ModelSliceEnum(str, Enum):
    COUNTRY_CURRENCY = "country_currency"
    EXCHANGE = "exchange"
    TICKER = "ticker"


SEED_ENTITIES: Dict[ModelSliceEnum, Tuple[bool, List[ModelSliceEnum]]] = {
    ModelSliceEnum.COUNTRY_CURRENCY: (True, []),
    ModelSliceEnum.EXCHANGE: (True, [ModelSliceEnum.COUNTRY_CURRENCY]),
    ModelSliceEnum.TICKER: (False, [ModelSliceEnum.EXCHANGE])
}
