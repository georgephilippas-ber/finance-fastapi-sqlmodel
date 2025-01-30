from typing import Dict, Any, List

from json import load
from os.path import join

from core.utilities.root import project_root


def read(path_elements: List[str]) -> Dict[str, Any]:
    with open(join(path_elements[0], *(path_elements[1:] if len(path_elements) > 1 else [])), 'r') as f:
        return load(f)
