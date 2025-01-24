enum EnvironmentType
{
    DEVELOPMENT,
    PRODUCTION
}

const SECURITY_ENABLED: boolean = false;

const FASTAPI_DEVELOPMENT_SERVER_BASE_URL = 'http://localhost:8000'
const FASTAPI_PRODUCTION_SERVER_BASE_URL = 'http://localhost:8000'

export const JSON_WEB_TOKEN_SECRET_KEY: string = 'bb07c2d34569be2cdf090daf5ae58daec3c998265d8685820288d620c3b279d2'

export const JSON_WEB_TOKEN_SECRET_KEY_ENCODED = new TextEncoder().encode(JSON_WEB_TOKEN_SECRET_KEY);

export const environment: EnvironmentType = EnvironmentType.DEVELOPMENT;

export const FASTAPI_SERVER_BASE_URL = environment == EnvironmentType.DEVELOPMENT ? FASTAPI_DEVELOPMENT_SERVER_BASE_URL : FASTAPI_PRODUCTION_SERVER_BASE_URL;

export const APPLICATION_NAVBAR_LOGO_URL = "https://flowbite.com/docs/images/logo.svg";

export const PROTECTED_ROUTES = SECURITY_ENABLED ? [
    '/members'
] : [];
