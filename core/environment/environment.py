from enum import Enum
from os.path import join
from os import getenv

from dotenv import load_dotenv

from core.utilities.root import project_root

ENVIRONMENT_LOADED: bool = False


def is_running_in_docker():
    return getenv("IN_DOCKER") == "true"


def load_environment() -> bool:
    global ENVIRONMENT_LOADED

    if ENVIRONMENT_LOADED:
        return True
    else:
        ENVIRONMENT_LOADED = True

        return load_dotenv(join(project_root(), 'secret', '.env'))


class EnvironmentType(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
