from enum import Enum
from typing import Dict, Tuple, List, Optional, TypeAlias

from pydantic.v1 import EmailStr

from configuration.environment import ENVIRONMENT
from configuration.project import PROJECT_NAME
from core.environment.environment import EnvironmentType
from schema.user.user import UserSchema

SEED_ON_STARTUP: bool = True


class ModelSliceEnum(str, Enum):
    COUNTRY_CURRENCY = "country_currency"
    GICS = "gics"
    EXCHANGE = "exchange"
    TICKER = "ticker"
    COMPANY_AND_COMPANY_SNAPSHOT_METRICS = "company_and_company_snapshot_metrics",
    USER = "user"
    MEILISEARCH_COMPANY_SEEDER = "meilisearch_company_seeder"
    FUNDAMENTAL_TIME_SERIES = "fundamental_time_series"


DROP_ALL_TABLES_BEFORE_SEEDING: bool = False

SeedSpecificationDict: TypeAlias = Dict[ModelSliceEnum, Tuple[bool, List[ModelSliceEnum]]]

SEED_ENTITIES_SPECIFICATION: SeedSpecificationDict = {
    ModelSliceEnum.COUNTRY_CURRENCY: (False, []),
    ModelSliceEnum.GICS: (False, []),
    ModelSliceEnum.EXCHANGE: (False, [ModelSliceEnum.COUNTRY_CURRENCY]),
    ModelSliceEnum.TICKER: (False, [ModelSliceEnum.EXCHANGE]),
    ModelSliceEnum.COMPANY_AND_COMPANY_SNAPSHOT_METRICS: (
        False, [ModelSliceEnum.TICKER, ModelSliceEnum.COUNTRY_CURRENCY, ModelSliceEnum.GICS, ModelSliceEnum.EXCHANGE]),
    ModelSliceEnum.USER: (False, []),
    ModelSliceEnum.MEILISEARCH_COMPANY_SEEDER: (False, [ModelSliceEnum.COMPANY_AND_COMPANY_SNAPSHOT_METRICS]),
    ModelSliceEnum.FUNDAMENTAL_TIME_SERIES: (True, [ModelSliceEnum.COMPANY_AND_COMPANY_SNAPSHOT_METRICS]),
}

COMPANY_SAMPLE_SIZE: Optional[int] = 20 if ENVIRONMENT == EnvironmentType.DEVELOPMENT else None

USERS: List[UserSchema] = [
    UserSchema(
        username="root",
        password="root!1A",
        email=EmailStr(f"root@{PROJECT_NAME}.org"),
    ),
    UserSchema(
        username="user",
        password="user!1A",
        email=EmailStr(f"user@{PROJECT_NAME}.org"),
    )
]
