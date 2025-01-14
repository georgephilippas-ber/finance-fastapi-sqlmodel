from os.path import join

from dotenv import load_dotenv

from configuration.root import project_root

ENVIRONMENT_LOADED: bool = False


def load_environment() -> bool:
    global ENVIRONMENT_LOADED

    if ENVIRONMENT_LOADED:
        return True
    else:
        ENVIRONMENT_LOADED = True

        return load_dotenv(join(project_root(), 'secret', '.env'))


if __name__ == '__main__':
    pass
