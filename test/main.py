import pytest
from os.path import join

from core.utilities.root import project_root

if __name__ == "__main__":
    pytest.main(["-s", join(project_root(), "test", "case")])
