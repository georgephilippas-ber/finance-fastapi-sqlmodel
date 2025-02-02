from configuration.environment import ENVIRONMENT, EnvironmentType
from core.environment.environment import is_running_in_docker

if is_running_in_docker():
    MEILISEARCH_SERVER_URL = 'http://meilisearch:7700'
else:
    if ENVIRONMENT == EnvironmentType.DEVELOPMENT:
        MEILISEARCH_SERVER_URL = 'http://127.0.0.1:7700'
    else:
        MEILISEARCH_SERVER_URL = 'http://127.0.0.1:7700'

MEILISEARCH_MASTER_KEY = "jYRlnO2U1liwOSdm9CjTPFS1HZuBjeaLK3gh2NXcr28"

SEED_HAS_RUN: bool = False
