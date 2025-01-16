enum EnvironmentType
{
    DEVELOPMENT,
    PRODUCTION
}

const FASTAPI_DEVELOPMENT_SERVER_BASE_URL = 'http://localhost:8000'
const FASTAPI_PRODUCTION_SERVER_BASE_URL = 'http://localhost:8000'

const environment: EnvironmentType = EnvironmentType.DEVELOPMENT;

export const FASTAPI_SERVER_BASE_URL = environment == EnvironmentType.DEVELOPMENT ? FASTAPI_DEVELOPMENT_SERVER_BASE_URL : FASTAPI_PRODUCTION_SERVER_BASE_URL;
