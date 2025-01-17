import pytest
from os.path import join

from core.utilities.root import project_root

pytest_args = ["-v", join(project_root(), "test", "case")]
exit_code = pytest.main(pytest_args)

if exit_code == 0:
    print("All tests passed!")
else:
    print("Some tests failed.")
