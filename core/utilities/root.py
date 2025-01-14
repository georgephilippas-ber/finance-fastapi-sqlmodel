from os import sep
from os.path import abspath

from configuration.project import PROJECT_NAME


def project_root() -> str:
    path_elements_ = abspath(__file__).split(sep)
    project_root_index_ = path_elements_.index(PROJECT_NAME)

    return sep.join(path_elements_[:project_root_index_ + 1])
