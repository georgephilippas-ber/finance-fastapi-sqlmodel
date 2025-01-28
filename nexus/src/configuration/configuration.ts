enum EnvironmentType
{
    DEVELOPMENT,
    PRODUCTION
}

export const ENVIRONMENT: EnvironmentType = EnvironmentType.DEVELOPMENT;

// SERVER

const FASTAPI_DEVELOPMENT_SERVER_BASE_URL = 'http://localhost:8000'
const FASTAPI_PRODUCTION_SERVER_BASE_URL = 'http://localhost:8000'

export const FASTAPI_SERVER_BASE_URL = ENVIRONMENT == EnvironmentType.DEVELOPMENT ? FASTAPI_DEVELOPMENT_SERVER_BASE_URL : FASTAPI_PRODUCTION_SERVER_BASE_URL;

const NEXUS_DEVELOPMENT_SERVER_BASE_URL = 'http://localhost:3000'
const NEXUS_PRODUCTION_SERVER_BASE_URL = 'http://localhost:3000'

export const NEXUS_SERVER_BASE_URL = ENVIRONMENT == EnvironmentType.DEVELOPMENT ? NEXUS_DEVELOPMENT_SERVER_BASE_URL : NEXUS_PRODUCTION_SERVER_BASE_URL;


// SECURITY
const SECURITY_ENABLED: boolean = true;

export const JSON_WEB_TOKEN_SECRET_KEY: string = 'bb07c2d34569be2cdf090daf5ae58daec3c998265d8685820288d620c3b279d2'

export const JSON_WEB_TOKEN_SECRET_KEY_ENCODED = new TextEncoder().encode(JSON_WEB_TOKEN_SECRET_KEY);

export const PROTECTED_ROUTES = SECURITY_ENABLED ? [
    '/members'
] : [];


// APPLICATION

export const APPLICATION_PROTECTED_HOME_URL = `${NEXUS_SERVER_BASE_URL}/members/company/search`;
export const APPLICATION_HOME_URL = `${NEXUS_SERVER_BASE_URL}`;
export const APPLICATION_NAVBAR_LOGO_URL = "https://flowbite.com/docs/images/logo.svg";


// INTERNATIONALIZATION

export const SUPPORTED_LOCALES = ['en', 'fr', 'de'];
