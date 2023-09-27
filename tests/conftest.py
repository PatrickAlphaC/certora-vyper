import pytest

from scripts.deploy_vault import deploy_vault
from scripts.helper_functions import get_account


@pytest.fixture
def vault():
    return deploy_vault()


@pytest.fixture
def account():
    return get_account()
