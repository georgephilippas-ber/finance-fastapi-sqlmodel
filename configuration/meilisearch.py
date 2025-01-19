from configuration.environment import ENVIRONMENT, EnvironmentType

if ENVIRONMENT == EnvironmentType.DEVELOPMENT:
    MEILISEARCH_SERVER_URL = 'http://127.0.0.1:7700'
else:
    MEILISEARCH_SERVER_URL = 'http://127.0.0.1:7700'

MEILISEARCH_MASTER_KEY = "jYRlnO2U1liwOSdm9CjTPFS1HZuBjeaLK3gh2NXcr28"
