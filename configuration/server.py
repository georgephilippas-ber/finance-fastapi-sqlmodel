from core.environment.environment import EnvironmentType
from configuration.root import ENVIRONMENT

NEXUS_DEVELOPMENT_SERVER: str = "http://localhost:3000"
NEXUS_PRODUCTION_SERVER: str = "http://localhost:3000"

NEXUS_SERVER: str = NEXUS_DEVELOPMENT_SERVER if ENVIRONMENT == EnvironmentType.DEVELOPMENT else NEXUS_PRODUCTION_SERVER
