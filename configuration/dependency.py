from enum import Enum
from typing import Dict, Tuple, List


class ModelSliceEnum(str, Enum):
    COUNTRY_CURRENCY = "country_currency"
    GICS = "gics"
    EXCHANGE = "exchange"
    TICKER = "ticker"
    COMPANY_AND_COMPANY_SNAPSHOT_METRICS = "company_and_company_snapshot_metrics"


SEED_ENTITIES: Dict[ModelSliceEnum, Tuple[bool, List[ModelSliceEnum]]] = {
    ModelSliceEnum.COUNTRY_CURRENCY: (True, []),
    ModelSliceEnum.GICS: (True, []),
    ModelSliceEnum.EXCHANGE: (False, [ModelSliceEnum.COUNTRY_CURRENCY]),
    ModelSliceEnum.TICKER: (False, [ModelSliceEnum.EXCHANGE]),
    ModelSliceEnum.COMPANY_AND_COMPANY_SNAPSHOT_METRICS: (
        True, [ModelSliceEnum.TICKER, ModelSliceEnum.COUNTRY_CURRENCY, ModelSliceEnum.GICS, ModelSliceEnum.EXCHANGE])
}
