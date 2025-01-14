from enum import Enum
from typing import Dict, Tuple, List, Optional

from configuration.root import EnvironmentType, ENVIRONMENT


class ModelSliceEnum(str, Enum):
    COUNTRY_CURRENCY = "country_currency"
    GICS = "gics"
    EXCHANGE = "exchange"
    TICKER = "ticker"
    COMPANY_AND_COMPANY_SNAPSHOT_METRICS = "company_and_company_snapshot_metrics"


DROP_ALL_TABLES_BEFORE_SEEDING: bool = True

SEED_ENTITIES: Dict[ModelSliceEnum, Tuple[bool, List[ModelSliceEnum]]] = {
    ModelSliceEnum.COUNTRY_CURRENCY: (True, []),
    ModelSliceEnum.GICS: (True, []),
    ModelSliceEnum.EXCHANGE: (True, [ModelSliceEnum.COUNTRY_CURRENCY]),
    ModelSliceEnum.TICKER: (True, [ModelSliceEnum.EXCHANGE]),
    ModelSliceEnum.COMPANY_AND_COMPANY_SNAPSHOT_METRICS: (
        True, [ModelSliceEnum.TICKER, ModelSliceEnum.COUNTRY_CURRENCY, ModelSliceEnum.GICS, ModelSliceEnum.EXCHANGE])
}

COMPANY_SAMPLE_SIZE: Optional[int] = 20 if ENVIRONMENT == EnvironmentType.DEVELOPMENT else None
