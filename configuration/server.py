from core.environment.environment import EnvironmentType, is_running_in_docker
from configuration.environment import ENVIRONMENT

NEXUS_DEVELOPMENT_SERVER: str = "http://localhost:3000"
NEXUS_PRODUCTION_SERVER: str = "http://localhost:3000"

NEXUS_DOCKER_SERVER: str = "http://frontend:3000"

NEXUS_SERVER: str = (
    NEXUS_DEVELOPMENT_SERVER if ENVIRONMENT == EnvironmentType.DEVELOPMENT else NEXUS_PRODUCTION_SERVER) if not is_running_in_docker() else NEXUS_DOCKER_SERVER
