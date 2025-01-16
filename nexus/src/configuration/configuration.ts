enum EnvironmentType
{
    DEVELOPMENT,
    PRODUCTION
}

const FASTAPI_DEVELOPMENT_SERVER_BASE_URL = 'http://localhost:8000'
const FASTAPI_PRODUCTION_SERVER_BASE_URL = 'http://localhost:8000'

const environment: EnvironmentType = EnvironmentType.DEVELOPMENT;

export const FASTAPI_SERVER_BASE_URL = environment == EnvironmentType.DEVELOPMENT ? FASTAPI_DEVELOPMENT_SERVER_BASE_URL : FASTAPI_PRODUCTION_SERVER_BASE_URL;

export const APPLICATION_NAVBAR_LOGO_URL = "https://flowbite.com/docs/images/logo.svg";
